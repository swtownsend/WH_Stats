import pandas as pd

import RollDice as rd


def hit_results(num_dice, weapon_df):
    pd.set_option('display.max_columns', None)
    hits_results_df = pd.DataFrame()

    for index, row in weapon_df.iterrows():

        if weapon_df["Rapid Fire"][index] == 1:
            dice = 2*(num_dice * weapon_df['Attacks'][index])
        else:

            dice = (num_dice * weapon_df['Attacks'][index])

        dice_results_df = rd.roll_results(weapon_df["Name"][index], dice)
        count_sr = dice_results_df.groupby(['Name', 'Dice Roll Results']).size()  # .groupby(level=0).max()
        count_df = pd.DataFrame(count_sr).reset_index()
        count_df.columns.values[2] = "counts"
        #print(count_df.head())
        # print(count_df.shape)

        Total_attacks = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]), 'counts'].sum()

        
        
        Success_hit = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                   (count_df['Dice Roll Results'] >= weapon_df['Weapon Skill'][
                                       index]), 'counts'].sum()

        
        # add crits
        crit_hit = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                (count_df['Dice Roll Results'] >= weapon_df['Crits'][index]), 'counts'].sum()

        # add sustained hits
        if type(weapon_df['Sustained hits'][index]) == str:
            sustained_hit_list = rd.roll_d3(crit_hit)
            # print('sustained_hit_list',sustained_hit_list)
            sustained_hit = int(sum(sustained_hit_list))
        else:
            sustained_hit = int((crit_hit * weapon_df['Sustained hits'][index]))

        Results_dict = ({"Name": weapon_df["Name"][index],
                         "Weapon Skill": weapon_df["Weapon Skill"][index],
                         "Weapon Attacks": weapon_df["Attacks"][index],
                         "Weapon Damage" : weapon_df["Damage"][index],
                         "Total Attacks": [Total_attacks],
                         "Num of Hits": [Success_hit],
                         "Num of Crits": [crit_hit],
                         "Sustained Hits": [sustained_hit],
                         "Weapon Sustained Hits":  weapon_df["Sustained hits"][index],
                         "Weapon Lethal Hit":  weapon_df["Lethal Hit"][index],
                         "Devastating Wound":  weapon_df["Devastating wound"][index],
                         "Mortal Wound":  weapon_df["Mortal wound"][index],
                         "Blast":  weapon_df["Blast"][index],
                         "Crits":  weapon_df["Crits"][index],
                         "Rapid Fire":  weapon_df["Rapid Fire"][index],
                         "Twin linked":  weapon_df["Twin_linked"][index]             
                         })

        # print("Results",Results_dict)
        hits_df = pd.DataFrame.from_dict(Results_dict)
        # print('hits df', hits_df)
        hits_results_df = pd.concat([hits_results_df, hits_df])

    hits_results_df.reset_index(drop=True, inplace=True)
    #print(hits_results_df.shape)

    return hits_results_df
