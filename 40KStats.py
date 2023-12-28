import pandas as pd

import HitResults as hr
import RsltAnalysis as dr
import SaveResults as sr
import WoundResults as wr


def main():
    pd.set_option('display.max_columns', None)
    total_hits_results_df = pd.DataFrame()
    total_wound_results_df = pd.DataFrame()
    total_save_results_df = pd.DataFrame()

    weapon_profile = {
                        "Name": ["HYlas Beam Cannon", "L7 Missle Lasuncher - Focused", "Sagitar Missle Lancher", "MATR autocannon"],
                        "Weapon Skill": [4, 4, 4, 4],
                        "Attacks": [2, 1, 2, 6],
                        "Weapon Str": [12, 9, 12, 7],
                        "Armour Pen": [0, -2, -3, -1],
                        "Damage": ["D6", "D6", 3, 2],
                        "Sustained hits": ["D3", 0, 0, 0],
                        "Lethal Hit": [0, 0, 0, 0],
                        "Devastating wound": [0, 0, 0, 0],
                        "Mortal wound": [0, 0, 0, 0],
                        "Blast": [0, 0, 0, 0],
                        "Crits": [6, 6, 6, 6],
                        "Rapid Fire": [0, 0, 0, 0],
                        "Twin_linked": [0, 0, 0, 0]
                        }

    sample_size = 100
    unit_size = 10
    reroll_1s = False  # True/False to reroll 1 for hit or wounds
    reroll_all = False  # True/False to reroll all for hit or wounds
    cover = False  # True/False if target has cover

    weapon_df = pd.DataFrame.from_dict(weapon_profile)
    weapon_df.reset_index(drop=True, inplace=True)

    for x in range(sample_size):
        hit_results_df = hr.hit_results(unit_size, weapon_df)
        total_hits_results_df = pd.concat([total_hits_results_df, hit_results_df])

        wounds_results_df = wr.wound_results(hit_results_df, weapon_df)
        total_wound_results_df = pd.concat([total_wound_results_df, wounds_results_df])

        save_results_df = sr.save_results(wounds_results_df, weapon_df)
        total_save_results_df = pd.concat([total_save_results_df, save_results_df])



    
    total_hits_results_df.to_excel('hits.xlsx')
    total_wound_results_df.to_excel('wounds.xlsx')
    total_save_results_df.to_excel('saves.xlsx')

    #dr.create_bargraph(weapon_df, total_hits_results_df, total_wound_results_df, total_save_results_df)

    #dr.create_attack_wnd_percent(weapon_df, total_hits_results_df, total_wound_results_df, total_save_results_df)

    #dr.merge_data(total_save_results_df)

if __name__ == "__main__":
    main()
