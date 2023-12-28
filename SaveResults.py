import pandas as pd
import RollDice as rd


def save_results(wound_df, weapon_df):
    global wounds
    global wound_rolls
    global saves
    global dev_wounds
    global dmg_dev_wounds
    pd.set_option('display.max_columns', None)
    save_results_df = pd.DataFrame()

    for index, row in wound_df.iterrows():

        # print(wound_df)
        dev_wounds = 0
        dmg_dev_wounds = 0

        if wound_df["Devastating Wound"][index] == 1:
            dev_wounds = int(wound_df['Wounds 6+'][index])
            dmg_dev_wounds = int(calc_dmg(wound_df['Weapon Damage'][index], dev_wounds))

        # if (wound_df['Name'][index] == wound_df['Name'][index]):

        for wnd in [2, 3, 4, 5, 6]:

            # calculate number of saves from wounds roll 
            if (wound_df['Wound Roll'][index] == wnd):
                wound_rolls = wound_df["Num of Successful Wounds"][index]

            wnd = int(wnd)

            dice = wound_rolls - dev_wounds

            dice_results_df = rd.roll_results(wound_df["Name"][index], dice=dice)

            count_df = roll_counts(dice_results_df)
            count_df.columns.values[2] = "counts"

            # dmg deal from failed saves at
            for sv in [2, 3, 4, 5, 6]:
                save_rolls = count_df.loc[(count_df['Name'] == wound_df["Name"][index]) &
                                          (count_df['Dice Roll Results'] >= sv), 'counts'].sum()

                # print('save roll',save_rolls)
                sucessful_wnds = int(wound_rolls - save_rolls)
                # print('sucessful_wnds',sucessful_wnds)
                dmg_caused = int(calc_dmg(wound_df['Weapon Damage'][index], sucessful_wnds, dev_wounds))
                # print('dmg caused', dmg_caused)

                sv = int(sv)
                # create dict of save and wound results
                sv_results_dict = ({"Name": wound_df["Name"][index],
                                    "Weapons Skill": wound_df["Weapons Skill"][index],
                                    "Weapon Attacks": wound_df["Weapon Attacks"][index],
                                    "Weapon Damage": wound_df["Weapon Damage"][index],
                                    "Weapon Sustained Hits": wound_df["Weapon Sustained Hits"][index],
                                    "Weapon Lethal Hit": wound_df["Weapon Lethal Hit"][index],
                                    "Devastating Wound": wound_df["Devastating Wound"][index],
                                    "Mortal Wound": wound_df["Mortal Wound"][index],
                                    "Blast": wound_df["Blast"][index],
                                    "Crits": wound_df["Crits"][index],
                                    "Rapid Fire": wound_df["Rapid Fire"][index],
                                    "Twin linked": wound_df["Twin linked"][index],
                                    "Total Attacks": wound_df["Total Attacks"][index],
                                    "Num of Hits": wound_df["Num of Hits"][index],
                                    "Num of Crits": wound_df["Num of Crits"][index],
                                    "Sustained Hits": wound_df["Sustained Hits"][index],
                                    "Total Hits": wound_df["Total Hits"][index],
                                    "Num Lethal Hits": wound_df["Num Lethal Hits"][index],
                                    'Wound Roll': wound_df['Wound Roll'][index],
                                    "Num of Successful Wounds": [sucessful_wnds],
                                    "Num of Wounds": [wound_rolls],
                                    "Save Roll": [sv],
                                    "Num of Saves Passed": [save_rolls],
                                    "Amt of Dmg": [dmg_caused],
                                    "Dev Wounds": [dev_wounds],
                                    "Dev Wounds Dmg": [dmg_dev_wounds]
                                    })

                # print("Results",Results_dict)
                save_df = pd.DataFrame.from_dict(sv_results_dict)
                # print('hits df', hits_df)
                save_results_df = pd.concat([save_results_df, save_df])

    save_results_df.reset_index(drop=True, inplace=True)
    # print('save results', save_results_df)
    return save_results_df


def roll_counts(dice_results_df):
    count_sr = dice_results_df.groupby(['Name', 'Dice Roll Results']).size()  # .groupby(level=0).max()
    count_df = pd.DataFrame(count_sr).reset_index()
    count_df.columns.values[2] = "counts"

    return count_df


def calc_dmg(wpn_dmg, wounds=1, dev_wounds=0):
    global dmg_caused
    if isinstance(wpn_dmg, str):
        if wpn_dmg[-1] == '6':
            sustained_hit_list = rd.roll_d6((wounds + dev_wounds))
            # print('sustained_hit_list',sustained_hit_list)
            dmg_caused = sum(sustained_hit_list)
        elif wpn_dmg[-1] == '3':
            sustained_hit_list = rd.roll_d3((wounds + dev_wounds))
            # print('sustained_hit_list',sustained_hit_list)
            dmg_caused = sum(sustained_hit_list)
    else:
        dmg_caused = (wounds + dev_wounds) * wpn_dmg

    return dmg_caused
