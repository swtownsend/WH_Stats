import pandas as pd
import RollDice as rd


def wound_results(hit_df, weapon_df):
    wound_results_df = pd.DataFrame()
    
    global wounds

    for index, row in hit_df.iterrows():

        dice_results_df = rd.roll_results(hit_df["Name"][index], dice=hit_df["Total Hits"][index])
        count_sr = dice_results_df.groupby(['Name', 'Dice Roll Results']).size()  # .groupby(level=0).max()
        count_df = pd.DataFrame(count_sr).reset_index()
        count_df.columns.values[2] = "counts"
        # print(count_df)
        # print(count_df.shape)

        
        for i in [2, 3, 4, 5, 6]:
            
            wounds = count_df.loc[(count_df['Name'] == hit_df["Name"][index]) &
                                    (count_df['Dice Roll Results'] >= i), 'counts'].sum()
            #print('wounds df wounds', wounds)
            Results_dict = ({"Name": [hit_df["Name"][index]],
                             "Weapons Skill": [hit_df["Weapon Skill"][index]],
                             "Weapon Attacks": [hit_df["Weapon Attacks"][index]],
                             "Weapon Damage" : [hit_df["Weapon Damage"][index]],
                             "Total Attacks":[hit_df["Total Attacks"][index]],
                             "Num of Hits": [hit_df["Num of Hits"][index]],
                             "Num of Crits":[hit_df["Num of Crits"][index]],
                             "Num Sustained Hits":[hit_df["Num Sustained Hits"][index]],
                             "Num Lethal Hits": [hit_df["Num Lethal Hits"][index]],
                             "Total Hits": [hit_df["Total Hits"][index]],
                             'Wound Roll': [i],
                             "Num of Successful Wounds": [wounds],
                             "Weapon Sustained Hits":  hit_df["Weapon Sustained Hits"][index],
                             "Weapon Lethal Hit":  hit_df["Weapon Lethal Hit"][index],
                             "Devastating Wound":  hit_df["Devastating Wound"][index],
                             "Mortal Wound":  hit_df["Mortal Wound"][index],
                             "Blast":  hit_df["Blast"][index],
                             "Crits":  hit_df["Crits"][index],
                             "Rapid Fire":  hit_df["Rapid Fire"][index],
                             "Twin linked":  hit_df["Twin linked"][index] 
                             })

            # print("Results",Results_dict)
            wounds_df = pd.DataFrame.from_dict(Results_dict)
            # print('hits df', hits_df)
            wound_results_df = pd.concat([wound_results_df, wounds_df])

    wound_results_df.reset_index(drop=True, inplace=True)
    #print("Num of Successful Wounds", wound_results_df["Num of Successful Wounds"])


    return wound_results_df
