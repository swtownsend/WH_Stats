import pandas as pd

import RollDice as rd


def save_results(wound_df, weapon_df):
    save_results_df = pd.DataFrame()
    wound_rolls = 0

    for index, row in weapon_df.iterrows():

        if (weapon_df["Devastating wound"][index] == 1):

            dev_wounds = wound_df['Wounds 6+'][index].astype(int)
            dmg_dev_wounds = calc_dmg(weapon_df['Damage'][index], dev_wounds)

        else:

            dev_wounds = 0
            dmg_dev_wounds = 0

        # calculate number of saves from wounds roll at 2+
        if (wound_df['Wound Roll'][index] == 2) & (weapon_df["Name"][index] == wound_df['Name'][index]):
            wound_rolls = wound_df["Num Successful Wounds"][index]

        dice = wound_rolls - dev_wounds
        dice_results_df = rd.roll_results(weapon_df["Name"][index], dice=dice)
        count_df = roll_counts(dice_results_df)

        # dmg deal from failed saves at 2+
        wnd2_save2 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                  (count_df['Dice Roll Results'] >= 2), 'counts'].sum()
        dmg_at_wnd2_save2 = calc_dmg(weapon_df['Damage'][index], wnd2_save2, dev_wounds)

        wnd2_save3 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                  (count_df['Dice Roll Results'] >= 3), 'counts'].sum()
        dmg_at_wnd2_save3 = calc_dmg(weapon_df['Damage'][index], wnd2_save3, dev_wounds)

        wnd2_save4 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                  (count_df['Dice Roll Results'] >= 4), 'counts'].sum()
        dmg_at_wnd2_save4 = calc_dmg(weapon_df['Damage'][index], wnd2_save4, dev_wounds)

        wnd2_save5 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                  (count_df['Dice Roll Results'] >= 5), 'counts'].sum()
        dmg_at_wnd2_save5 = calc_dmg(weapon_df['Damage'][index], wnd2_save5, dev_wounds)

        wnd2_save6 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                  (count_df['Dice Roll Results'] >= 6), 'counts'].sum()
        dmg_at_wnd2_save6 = calc_dmg(weapon_df['Damage'][index], wnd2_save6, dev_wounds)

        # calculate number of saves from wounds roll at 3+
        if (wound_df['Wound Roll'][index] == 3) & (weapon_df["Name"][index] == wound_df['Name'][index]):
            wound_rolls = wound_df["Num Successful Wounds"][index]

        dice = wound_rolls - dev_wounds
        dice_results_df = rd.roll_results(weapon_df["Name"][index], dice=dice)
        count_df = roll_counts(dice_results_df)

        wnd3_save2 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                  (count_df['Dice Roll Results'] >= 2), 'counts'].sum()
        dmg_at_wnd3_save2 = calc_dmg(weapon_df['Damage'][index], wnd3_save2, dev_wounds)

        wnd3_save3 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                  (count_df['Dice Roll Results'] >= 3), 'counts'].sum()
        dmg_at_wnd3_save3 = calc_dmg(weapon_df['Damage'][index], wnd3_save3, dev_wounds)

        wnd3_save4 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                  (count_df['Dice Roll Results'] >= 4), 'counts'].sum()
        dmg_at_wnd3_save4 = calc_dmg(weapon_df['Damage'][index], wnd3_save4, dev_wounds)

        wnd3_save5 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                  (count_df['Dice Roll Results'] >= 5), 'counts'].sum()
        dmg_at_wnd3_save5 = calc_dmg(weapon_df['Damage'][index], wnd3_save5, dev_wounds)

        wnd3_save6 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                  (count_df['Dice Roll Results'] >= 6), 'counts'].sum()
        dmg_at_wnd3_save6 = calc_dmg(weapon_df['Damage'][index], wnd2_save6, dev_wounds)

        # calculate number of saves from wounds roll at 4+
        if (wound_df['Wound Roll'][index] == 4) & (weapon_df["Name"][index] == wound_df['Name'][index]):
            wound_rolls = wound_df["Num Successful Wounds"][index]

        dice = wound_rolls - dev_wounds
        dice_results_df = rd.roll_results(weapon_df["Name"][index], dice=dice)
        count_df = roll_counts(dice_results_df)

        wnd4_save2 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                  (count_df['Dice Roll Results'] >= 2), 'counts'].sum()
        dmg_at_wnd4_save2 = calc_dmg(weapon_df['Damage'][index], wnd4_save2, dev_wounds)

        wnd4_save3 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                  (count_df['Dice Roll Results'] >= 3), 'counts'].sum()
        dmg_at_wnd4_save3 = calc_dmg(weapon_df['Damage'][index], wnd4_save3, dev_wounds)

        wnd4_save4 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                  (count_df['Dice Roll Results'] >= 4), 'counts'].sum()
        dmg_at_wnd4_save4 = calc_dmg(weapon_df['Damage'][index], wnd4_save4, dev_wounds)

        wnd4_save5 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                  (count_df['Dice Roll Results'] >= 5), 'counts'].sum()
        dmg_at_wnd4_save5 = calc_dmg(weapon_df['Damage'][index], wnd4_save5, dev_wounds)

        wnd4_save6 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                  (count_df['Dice Roll Results'] >= 6), 'counts'].sum()
        dmg_at_wnd4_save6 = calc_dmg(weapon_df['Damage'][index], wnd4_save6, dev_wounds)

        # calculate number of saves from wounds roll at 5+
        if (wound_df['Wound Roll'][index] == 5) & (weapon_df["Name"][index] == wound_df['Name'][index]):
            wound_rolls = wound_df["Num Successful Wounds"][index]

        dice = wound_rolls - dev_wounds
        dice_results_df = rd.roll_results(weapon_df["Name"][index], dice=dice)
        count_df = roll_counts(dice_results_df)

        wnd5_save2 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                  (count_df['Dice Roll Results'] >= 2), 'counts'].sum()
        dmg_at_wnd5_save2 = calc_dmg(weapon_df['Damage'][index], wnd5_save2, dev_wounds)

        wnd5_save3 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                  (count_df['Dice Roll Results'] >= 3), 'counts'].sum()
        dmg_at_wnd5_save3 = calc_dmg(weapon_df['Damage'][index], wnd5_save3, dev_wounds)

        wnd5_save4 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                  (count_df['Dice Roll Results'] >= 4), 'counts'].sum()
        dmg_at_wnd5_save4 = calc_dmg(weapon_df['Damage'][index], wnd5_save4, dev_wounds)

        wnd5_save5 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                  (count_df['Dice Roll Results'] >= 5), 'counts'].sum()
        dmg_at_wnd5_save5 = calc_dmg(weapon_df['Damage'][index], wnd5_save5, dev_wounds)

        wnd5_save6 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                  (count_df['Dice Roll Results'] >= 6), 'counts'].sum()
        dmg_at_wnd5_save6 = calc_dmg(weapon_df['Damage'][index], wnd5_save6, dev_wounds)

        # calculate number of saves from wounds roll at 6+
        if (wound_df['Wound Roll'][index] == 6) & (weapon_df["Name"][index] == wound_df['Name'][index]):
            wound_rolls = wound_df["Num Successful Wounds"][index]

        dice = wound_rolls - dev_wounds
        dice_results_df = rd.roll_results(weapon_df["Name"][index], dice=dice)
        count_df = roll_counts(dice_results_df)

        wnd6_save2 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                  (count_df['Dice Roll Results'] >= 2), 'counts'].sum()
        dmg_at_wnd6_save2 = calc_dmg(weapon_df['Damage'][index], wnd6_save2)

        wnd6_save3 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                  (count_df['Dice Roll Results'] >= 3), 'counts'].sum()
        dmg_at_wnd6_save3 = calc_dmg(weapon_df['Damage'][index], wnd6_save3)

        wnd6_save4 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                  (count_df['Dice Roll Results'] >= 4), 'counts'].sum()
        dmg_at_wnd6_save4 = calc_dmg(weapon_df['Damage'][index], wnd6_save4)

        wnd6_save5 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                  (count_df['Dice Roll Results'] >= 5), 'counts'].sum()
        dmg_at_wnd6_save5 = calc_dmg(weapon_df['Damage'][index], wnd6_save5)

        wnd6_save6 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                  (count_df['Dice Roll Results'] >= 6), 'counts'].sum()
        dmg_at_wnd6_save6 = calc_dmg(weapon_df['Damage'][index], wnd6_save6, dev_wounds)

        # create dict of save and wound results
        sv_results_dict = ({"Name": weapon_df["Name"][index],
                            "Wound Roll": [2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6],
                            "Save Roll": [2, 3, 4, 5, 6, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6],
                            "Num of Successful Saves": [wnd2_save2, wnd2_save3, wnd2_save4, wnd2_save5, wnd2_save6,
                                                        wnd3_save2, wnd3_save3, wnd3_save4, wnd3_save5, wnd3_save6,
                                                        wnd4_save2, wnd4_save3, wnd4_save4, wnd4_save5, wnd4_save6,
                                                        wnd5_save2, wnd5_save3, wnd5_save4, wnd5_save5, wnd5_save6,
                                                        wnd6_save2, wnd6_save3, wnd6_save4, wnd6_save5, wnd6_save6],
                            "Amt of Dmg": [dmg_at_wnd2_save2, dmg_at_wnd2_save3, dmg_at_wnd2_save4, dmg_at_wnd2_save5,
                                           dmg_at_wnd2_save6,
                                           dmg_at_wnd3_save2, dmg_at_wnd3_save3, dmg_at_wnd3_save4, dmg_at_wnd3_save5,
                                           dmg_at_wnd3_save6,
                                           dmg_at_wnd4_save2, dmg_at_wnd4_save3, dmg_at_wnd4_save4, dmg_at_wnd4_save5,
                                           dmg_at_wnd4_save6,
                                           dmg_at_wnd5_save2, dmg_at_wnd5_save3, dmg_at_wnd5_save4, dmg_at_wnd5_save5,
                                           dmg_at_wnd5_save6,
                                           dmg_at_wnd6_save2, dmg_at_wnd6_save3, dmg_at_wnd6_save4, dmg_at_wnd6_save5,
                                           dmg_at_wnd6_save6],
                            "Dev Wounds": [dev_wounds, dev_wounds, dev_wounds, dev_wounds, dev_wounds,
                                           dev_wounds, dev_wounds, dev_wounds, dev_wounds, dev_wounds,
                                           dev_wounds, dev_wounds, dev_wounds, dev_wounds, dev_wounds,
                                           dev_wounds, dev_wounds, dev_wounds, dev_wounds, dev_wounds,
                                           dev_wounds, dev_wounds, dev_wounds, dev_wounds, dev_wounds],
                            "Dev Wounds Dmg": [dmg_dev_wounds, dmg_dev_wounds, dmg_dev_wounds, dmg_dev_wounds,
                                               dmg_dev_wounds,
                                               dmg_dev_wounds, dmg_dev_wounds, dmg_dev_wounds, dmg_dev_wounds,
                                               dmg_dev_wounds,
                                               dmg_dev_wounds, dmg_dev_wounds, dmg_dev_wounds, dmg_dev_wounds,
                                               dmg_dev_wounds,
                                               dmg_dev_wounds, dmg_dev_wounds, dmg_dev_wounds, dmg_dev_wounds,
                                               dmg_dev_wounds,
                                               dmg_dev_wounds, dmg_dev_wounds, dmg_dev_wounds, dmg_dev_wounds,
                                               dmg_dev_wounds]
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
    dmg_caused = 0

    if isinstance(wpn_dmg, str) == True:
        if wpn_dmg[-1] == '6':
            sustained_hit_list = rd.roll_d3((wounds + dev_wounds))
            # print('sustained_hit_list',sustained_hit_list)
            dmg_caused = sum(sustained_hit_list)
        elif wpn_dmg[-1] == '3':
            sustained_hit_list = rd.roll_d3((wounds + dev_wounds))
            # print('sustained_hit_list',sustained_hit_list)
            dmg_caused = sum(sustained_hit_list)
    else:
        dmg_caused = (wounds + dev_wounds) * wpn_dmg

    return dmg_caused
