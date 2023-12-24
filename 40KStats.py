import pandas as pd
import HitResults as hr
import WoundResults as wr
import SaveResults as sr
import RsltAnalysis as dr

def main():
    total_hits_results_df = pd.DataFrame()
    total_wound_results_df = pd.DataFrame()
    total_save_results_df = pd.DataFrame()


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

    sample_size = 10
    unit_size = 10
    reroll_1s = False # True/False to reroll 1 for hit or wounds
    reroll_all = False # True/False to reroll all for hit or wounds
    cover = False # True/False if target has cover

    weapon_df = pd.DataFrame.from_dict(weapon_profile)

    for x in range(sample_size):
        hit_results_df = hr.hit_results(unit_size,weapon_df)
        total_hits_results_df = pd.concat([total_hits_results_df,hit_results_df])

        wounds_results_df = wr.wound_results(hit_results_df,weapon_df)
        total_wound_results_df = pd.concat([total_wound_results_df ,wounds_results_df])

        save_results_df = sr.save_results(wounds_results_df,weapon_df)
        total_save_results_df = pd.concat([total_save_results_df ,save_results_df])

    dr.create_bargraph(weapon_df, total_hits_results_df, total_wound_results_df, total_save_results_df)

if __name__ == "__main__":
    main()
