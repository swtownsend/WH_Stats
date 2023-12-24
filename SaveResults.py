import pandas as pd
from sympy.strategies.core import switch

import RollDice as rd

def save_results(wound_df, weapon_df):

    save_results_df = pd.DataFrame()

    for index, row in weapon_df.iterrows():

        if (weapon_df["Devastating wound"][index] == 1):

            dev_wounds = wound_df['Wounds 6+'][index].astype(int)
            dmg_dev_wounds = calc_dmg(weapon_df['Damage'][index].astype(int), dev_wounds)
            save_2v6 = save_3v6 = save_4v6 = save_5v6 = save_6v2 = save_6v3 = save_6v4 = save_6v5 = save_6v6 = 0
            dmg_2v6 = dmg_3v6 = dmg_4v6 = dmg_5v6 = dmg_6v2 = dmg_6v3 = dmg_6v4 = dmg_6v5 = dmg_6v6 = 0

            dice = (wound_df['Wounds 2+'][index].astype(int) - wound_df['Wounds 6+'][index].astype(int))
            dice_results_df = rd.roll_results(weapon_df["Name"][index], dice=dice)
            count_df = roll_counts(dice_results_df )
            save_2v2 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                (count_df['Dice Roll Results'] >= 2), 'counts'].sum()
            dmg_2v2 = calc_dmg(weapon_df['Damage'][index].astype(int),save_2v2,dev_wounds)
            save_2v3 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                    (count_df['Dice Roll Results'] >= 3), 'counts'].sum()
            dmg_2v3 = calc_dmg(weapon_df['Damage'][index].astype(int), save_2v3, dev_wounds)
            save_2v4 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                    (count_df['Dice Roll Results'] >= 4), 'counts'].sum()
            dmg_2v4 = calc_dmg(weapon_df['Damage'][index].astype(int), save_2v4, dev_wounds)
            save_2v5 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                    (count_df['Dice Roll Results'] >= 5), 'counts'].sum()
            dmg_2v5 = calc_dmg(weapon_df['Damage'][index].astype(int), save_2v5, dev_wounds)

            dice = (wound_df['Wounds 3+'][index].astype(int) - wound_df['Wounds 6+'][index].astype(int))
            dice_results_df = rd.roll_results(weapon_df["Name"][index], dice=dice)
            count_df = roll_counts(dice_results_df)
            save_3v2 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                  (count_df['Dice Roll Results'] >= 2), 'counts'].sum()
            dmg_3v2 = calc_dmg(weapon_df['Damage'][index].astype(int), save_3v2, dev_wounds)
            save_3v3 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                    (count_df['Dice Roll Results'] >= 3), 'counts'].sum()
            dmg_3v3 = calc_dmg(weapon_df['Damage'][index].astype(int), save_3v3, dev_wounds)
            save_3v4 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                    (count_df['Dice Roll Results'] >= 4), 'counts'].sum()
            dmg_3v4 = calc_dmg(weapon_df['Damage'][index].astype(int), save_3v4, dev_wounds)
            save_3v5 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                    (count_df['Dice Roll Results'] >= 5), 'counts'].sum()
            dmg_3v5 = calc_dmg(weapon_df['Damage'][index].astype(int), save_3v5, dev_wounds)

            dice = (wound_df['Wounds 4+'][index].astype(int) - wound_df['Wounds 6+'][index].astype(int))
            dice_results_df = rd.roll_results(weapon_df["Name"][index], dice=dice)
            count_df = roll_counts(dice_results_df)
            save_4v2 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                    (count_df['Dice Roll Results'] >= 2), 'counts'].sum()
            dmg_4v2 = calc_dmg(weapon_df['Damage'][index].astype(int), save_4v2, dev_wounds)
            save_4v3 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                    (count_df['Dice Roll Results'] >= 3), 'counts'].sum()
            dmg_4v3 = calc_dmg(weapon_df['Damage'][index].astype(int), save_4v3, dev_wounds)
            save_4v4 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                    (count_df['Dice Roll Results'] >= 4), 'counts'].sum()
            dmg_4v4 = calc_dmg(weapon_df['Damage'][index].astype(int), save_4v4, dev_wounds)
            save_4v5 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                    (count_df['Dice Roll Results'] >= 5), 'counts'].sum()
            dmg_4v5 = calc_dmg(weapon_df['Damage'][index].astype(int), save_4v5, dev_wounds)

            dice = (wound_df['Wounds 5+'][index].astype(int) - wound_df['Wounds 6+'][index].astype(int))
            dice_results_df = rd.roll_results(weapon_df["Name"][index], dice=dice)
            count_df = roll_counts(dice_results_df)
            save_5v2 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                    (count_df['Dice Roll Results'] >= 2), 'counts'].sum()
            dmg_5v2 = calc_dmg(weapon_df['Damage'][index].astype(int), save_5v2, dev_wounds)
            save_5v3 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                    (count_df['Dice Roll Results'] >= 3), 'counts'].sum()
            dmg_5v3 = calc_dmg(weapon_df['Damage'][index].astype(int), save_5v3, dev_wounds)
            save_5v4 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                    (count_df['Dice Roll Results'] >= 4), 'counts'].sum()
            dmg_5v4 = calc_dmg(weapon_df['Damage'][index].astype(int), save_5v4, dev_wounds)
            save_5v5 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                    (count_df['Dice Roll Results'] >= 5), 'counts'].sum()
            dmg_5v5 = calc_dmg(weapon_df['Damage'][index].astype(int), save_5v5, dev_wounds)

        else:
            dev_wounds = 0
            dmg_dev_wounds = 0

            dice = (wound_df['Wounds 2+'][index].astype(int))
            dice_results_df = rd.roll_results(weapon_df["Name"][index], dice=dice)
            count_df = roll_counts(dice_results_df)
            save_2v2 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                   (count_df['Dice Roll Results'] >= 2), 'counts'].sum()
            dmg_2v2 = calc_dmg(weapon_df['Damage'][index].astype(int), save_2v2)
            save_2v3 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                   (count_df['Dice Roll Results'] >= 3), 'counts'].sum()
            dmg_2v3 = calc_dmg(weapon_df['Damage'][index].astype(int), save_2v3)
            save_2v4 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                   (count_df['Dice Roll Results'] >= 4), 'counts'].sum()
            dmg_2v4 = calc_dmg(weapon_df['Damage'][index].astype(int), save_2v4)
            save_2v5 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                   (count_df['Dice Roll Results'] >= 5), 'counts'].sum()
            dmg_2v5 = calc_dmg(weapon_df['Damage'][index].astype(int), save_2v5)
            save_2v6 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                   (count_df['Dice Roll Results'] >= 6), 'counts'].sum()
            dmg_2v6 = calc_dmg(weapon_df['Damage'][index].astype(int), save_2v6)

            dice = (wound_df['Wounds 3+'][index].astype(int))
            dice_results_df = rd.roll_results(weapon_df["Name"][index], dice=dice)
            count_df = roll_counts(dice_results_df)
            save_3v2 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                   (count_df['Dice Roll Results'] >= 2), 'counts'].sum()
            dmg_3v2 = calc_dmg(weapon_df['Damage'][index].astype(int), save_3v2)
            save_3v3 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                   (count_df['Dice Roll Results'] >= 3), 'counts'].sum()
            dmg_3v3 = calc_dmg(weapon_df['Damage'][index].astype(int), save_3v3)
            save_3v4 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                   (count_df['Dice Roll Results'] >= 4), 'counts'].sum()
            dmg_3v4 = calc_dmg(weapon_df['Damage'][index].astype(int), save_3v4)
            save_3v5 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                   (count_df['Dice Roll Results'] >= 5), 'counts'].sum()
            dmg_3v5 = calc_dmg(weapon_df['Damage'][index].astype(int), save_3v5)
            save_3v6 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                   (count_df['Dice Roll Results'] >= 6), 'counts'].sum()
            dmg_3v6 = calc_dmg(weapon_df['Damage'][index].astype(int), save_3v6)

            dice = (wound_df['Wounds 4+'][index].astype(int))
            dice_results_df = rd.roll_results(weapon_df["Name"][index], dice=dice)
            count_df = roll_counts(dice_results_df)
            save_4v2 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                   (count_df['Dice Roll Results'] >= 2), 'counts'].sum()
            dmg_4v2 = calc_dmg(weapon_df['Damage'][index].astype(int), save_4v2)
            save_4v3 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                   (count_df['Dice Roll Results'] >= 3), 'counts'].sum()
            dmg_4v3 = calc_dmg(weapon_df['Damage'][index].astype(int), save_4v3)
            save_4v4 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                   (count_df['Dice Roll Results'] >= 4), 'counts'].sum()
            dmg_4v4 = calc_dmg(weapon_df['Damage'][index].astype(int), save_4v4)
            save_4v5 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                   (count_df['Dice Roll Results'] >= 5), 'counts'].sum()
            dmg_4v5 = calc_dmg(weapon_df['Damage'][index].astype(int), save_4v5)
            save_4v6 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                   (count_df['Dice Roll Results'] >= 6), 'counts'].sum()
            dmg_4v6 = calc_dmg(weapon_df['Damage'][index].astype(int), save_4v6)

            dice = (wound_df['Wounds 5+'][index].astype(int))
            dice_results_df = rd.roll_results(weapon_df["Name"][index], dice=dice)
            count_df = roll_counts(dice_results_df)
            save_5v2 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                   (count_df['Dice Roll Results'] >= 2), 'counts'].sum()
            dmg_5v2 = calc_dmg(weapon_df['Damage'][index].astype(int), save_5v2)
            save_5v3 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                   (count_df['Dice Roll Results'] >= 3), 'counts'].sum()
            dmg_5v3 = calc_dmg(weapon_df['Damage'][index].astype(int), save_5v3)
            save_5v4 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                   (count_df['Dice Roll Results'] >= 4), 'counts'].sum()
            dmg_5v4 = calc_dmg(weapon_df['Damage'][index].astype(int), save_5v4)
            save_5v5 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                   (count_df['Dice Roll Results'] >= 5), 'counts'].sum()
            dmg_5v5 = calc_dmg(weapon_df['Damage'][index].astype(int), save_5v5)
            save_5v6 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                   (count_df['Dice Roll Results'] >= 6), 'counts'].sum()
            dmg_5v6 = calc_dmg(weapon_df['Damage'][index].astype(int), save_5v6)

            dice = (wound_df['Wounds 6+'][index].astype(int))
            dice_results_df = rd.roll_results(weapon_df["Name"][index], dice=dice)
            count_df = roll_counts(dice_results_df)
            save_6v2 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                   (count_df['Dice Roll Results'] >= 2), 'counts'].sum()
            dmg_6v2 = calc_dmg(weapon_df['Damage'][index].astype(int), save_6v2)
            save_6v3 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                   (count_df['Dice Roll Results'] >= 3), 'counts'].sum()
            dmg_6v3 = calc_dmg(weapon_df['Damage'][index].astype(int), save_6v3)
            save_6v4 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                   (count_df['Dice Roll Results'] >= 4), 'counts'].sum()
            dmg_6v4 = calc_dmg(weapon_df['Damage'][index].astype(int), save_6v4)
            save_6v5 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                   (count_df['Dice Roll Results'] >= 5), 'counts'].sum()
            dmg_6v5 = calc_dmg(weapon_df['Damage'][index].astype(int), save_6v5)
            save_6v6 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                   (count_df['Dice Roll Results'] >= 6), 'counts'].sum()
            dmg_6v6 = calc_dmg(weapon_df['Damage'][index].astype(int), save_6v6)


        sv_results_dict = ({"Name": weapon_df["Name"][index],
                            "Dev Wounds": [dev_wounds],
                            "Dev Wounds Dmg": [dmg_dev_wounds],
                            "Save 2+ vs Wound 2+": [save_2v2],
                            "Dmg 2v2": [dmg_2v2],
                            "Save 2+ vs Wound 3+": [save_2v3],
                            "Dmg 2v3": [dmg_2v3],
                            "Save 2+ vs Wound 4+": [save_2v4],
                            "Dmg 2v4": [dmg_2v4],
                            "Save 2+ vs Wound 5+": [save_2v5],
                            "Dmg 2v5": [dmg_2v5],
                            "Save 2+ vs Wound 6+": [save_2v6],
                            "Dmg 2v6": [dmg_2v6],
                            "Save 3+ vs Wound 2+": [save_3v2],
                            "Dmg 3v2": [dmg_3v2],
                            "Save 3+ vs Wound 3+": [save_3v3],
                            "Dmg 3v3": [dmg_3v3],
                            "Save 3+ vs Wound 4+": [save_3v4],
                            "Dmg 3v4": [dmg_3v4],
                            "Save 3+ vs Wound 5+": [save_3v5],
                            "Dmg 3v5": [dmg_3v5],
                            "Save 3+ vs Wound 6+": [save_3v6],
                            "Dmg 3v6": [dmg_3v6],
                            "Save 4+ vs Wound 2+": [save_4v2],
                            "Dmg 4v2": [dmg_4v2],
                            "Save 4+ vs Wound 3+": [save_4v3],
                            "Dmg 4v3": [dmg_4v3],
                            "Save 4+ vs Wound 4+": [save_4v4],
                            "Dmg 4v4": [dmg_4v4],
                            "Save 4+ vs Wound 5+": [save_4v5],
                            "Dmg 4v5": [dmg_4v5],
                            "Save 4+ vs Wound 6+": [save_4v6],
                            "Dmg 4v6": [dmg_4v6],
                            "Save 5+ vs Wound 2+": [save_5v2],
                            "Dmg 5v2": [dmg_5v2],
                            "Save 5+ vs Wound 3+": [save_5v3],
                            "Dmg 5v3": [dmg_5v3],
                            "Save 5+ vs Wound 4+": [save_5v4],
                            "Dmg 5v4": [dmg_5v4],
                            "Save 5+ vs Wound 5+": [save_5v5],
                            "Dmg 5v5": [dmg_5v5],
                            "Save 5+ vs Wound 6+": [save_5v6],
                            "Dmg 5v6": [dmg_5v6],
                            "Save 6+ vs Wound 2+": [save_6v2],
                            "Dmg 6v2": [dmg_6v2],
                            "Save 6+ vs Wound 3+": [save_6v3],
                            "Dmg 6v3": [dmg_6v3],
                            "Save 6+ vs Wound 4+": [save_6v4],
                            "Dmg 6v4": [dmg_6v4],
                            "Save 6+ vs Wound 5+": [save_6v5],
                            "Dmg 6v5": [dmg_6v5],
                            "Save 6+ vs Wound 6+": [save_6v6],
                            "Dmg 6v6": [dmg_6v6],
                         })

        # print("Results",Results_dict)
        save_df = pd.DataFrame.from_dict(sv_results_dict)
        # print('hits df', hits_df)
        save_results_df = pd.concat([save_results_df, save_df])

    save_results_df.reset_index(drop=True, inplace=True)
    print('save results',save_results_df)
    return save_results_df

def roll_counts(dice_results_df):

    count_sr = dice_results_df.groupby(['Name', 'Dice Roll Results']).size()  # .groupby(level=0).max()
    count_df = pd.DataFrame(count_sr).reset_index()
    count_df.columns.values[2] = "counts"

    return count_df

def calc_dmg(wpn_dmg,wounds=1,dev_wounds=0):
    dmg_caused = 0

    if isinstance(wpn_dmg,str) == True:
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
