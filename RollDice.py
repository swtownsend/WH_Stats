import pandas as pd
import random


def roll_results(weapon_name,dice=1):

    dice_results_df = pd.DataFrame()


    #for index, row in weapon_df.iterrows():

        #num_dice = dice * weapon_df['Attacks'][index]

    roll_results = roll_d6(dice)
        # print('roll result', roll_results)

    dice_dict =({"Name": weapon_name,
                        "Dice Roll Results": roll_results,
                        })

        # 3print('attack dict', attack_dict)
    dice_df = pd.DataFrame.from_dict(dice_dict)
        # print('attack df', attack_df)

    dice_results_df = pd.concat([dice_results_df, dice_df])
        # print('attack_results_df',attack_results_df)

    return dice_results_df


def roll_d6(num_dice):
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_results

def roll_d3(num_dice):
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1, 3)
        roll_results.append(roll)
    return roll_results