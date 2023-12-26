import pandas as pd

import RollDice as rd


def wound_results(hit_df, weapon_df):
    wound_results_df = pd.DataFrame()

    for index, row in weapon_df.iterrows():

        if (weapon_df["Lethal Hit"][index] == 1):
            dice = ((hit_df['Num of hits'][index].astype(int) -
                     hit_df['Num of crits'][index].astype(int)) + hit_df['Sustained Hits'][index].astype(int))

            lethal_hit = hit_df['Num of crits'][index]

        else:

            dice = (hit_df['Num of hits'][index].astype(int)) + hit_df['Sustained Hits'][index].astype(int)
            lethal_hit = 0

        dice_results_df = rd.roll_results(weapon_df["Name"][index], dice=dice)
        count_sr = dice_results_df.groupby(['Name', 'Dice Roll Results']).size()  # .groupby(level=0).max()
        count_df = pd.DataFrame(count_sr).reset_index()
        count_df.columns.values[2] = "counts"
        # print(count_df)
        # print(count_df.shape)

        wounds_2 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                (count_df['Dice Roll Results'] >= 2), 'counts'].sum()
        wounds_3 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                (count_df['Dice Roll Results'] >= 3), 'counts'].sum()
        wounds_4 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                (count_df['Dice Roll Results'] >= 4), 'counts'].sum()
        wounds_5 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                (count_df['Dice Roll Results'] >= 5), 'counts'].sum()
        wounds_6 = count_df.loc[(count_df['Name'] == weapon_df["Name"][index]) &
                                (count_df['Dice Roll Results'] >= 6), 'counts'].sum()

        Results_dict = ({"Name": [weapon_df["Name"][index],weapon_df["Name"][index],weapon_df["Name"][index],weapon_df["Name"][index],weapon_df["Name"][index]],
                         "Total hits": [dice,dice,dice,dice,dice],
                         "Lethal hits": [lethal_hit,lethal_hit,lethal_hit,lethal_hit,lethal_hit],
                         'Wound Roll': [2,3,4,5,6],
                         "Num Successful Wounds": [wounds_2,wounds_3,wounds_4,wounds_5,wounds_6],
                         })

        # print("Results",Results_dict)
        wounds_df = pd.DataFrame.from_dict(Results_dict)
        # print('hits df', hits_df)
        wound_results_df = pd.concat([wound_results_df, wounds_df])

    wound_results_df.reset_index(drop=True, inplace=True)

    return wound_results_df
