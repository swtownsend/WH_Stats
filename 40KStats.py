import pandas as pd
import matplotlib.pyplot as plt
import random

import HitResults as hr
import WoundResults as wr
import SaveResults as sr
import RsltAnalysis as dr
import RollDice as rd

def main():

    weapon_profile = {"Name": ["Volkanite disintergrator","EtaCarn Plasma gun"],
                    "Weapon Skill": [3,3],
                    "Attacks":[3,1],
                    "Weapon Str":[5,8] ,
                    "Armour Pen":[0,-3],
                    "Damage":[1,3],
                    "Sustained hits":[0,0],
                    "Lethal Hit":[0,1],
                    "Devastating wound":[1,0],
                    "Mortal wound":[0,0],
                    "Blast":[0,0],
                    "Crits":[6,6]
                    }

    num_dice = 100
    unit_size = [1,5,10,15,20]
    reroll_1s = False # True/False to reroll 1 for hit or wounds
    reroll_all = False # True/False to reroll all for hit or wounds
    cover = False # True/False if target has cover

    weapon_df = pd.DataFrame.from_dict(weapon_profile)

    hit_results_df = hr.hit_results(num_dice,weapon_df)
    print("hit_results_df",hit_results_df)

    wounds_results_df = wr.wound_results(hit_results_df,weapon_df)
    print("wound results",wounds_results_df)

    save_results_df = sr.save_results(wounds_results_df,weapon_df)

    dr.create_bargraph(weapon_df, hit_results_df, wounds_results_df, save_results_df)

if __name__ == "__main__":
    main()
