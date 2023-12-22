import pandas as pd
import matplotlib.pyplot as plt
import random
from pprint import pprint

def main():

    weapon_profile = {"Name": ["Volkanite disintergrator","EtaCarn Plasma gun"],
                    "Weapon Skill": [3,3],
                    "Attacks":[3,1],
                    "Weapon Str":[5,8] ,
                    "Armour Pen":[0,-3],
                    "Damage":[1,3],
                    "Sustained hits":[0,0],
                    "Lethal Hit":[0,0],
                    "Devastating wound":[1,0],
                    "Mortal wound":[0,0],
                    "Blast":[0,0],
                    "Crits":[6,6]
                    }

    num_attacks = 100
    unit_size = [1,5,10,15,20]
    reroll_1s = False # True/False to reroll 1 for hit or wounds
    reroll_all = False # True/False to reroll all for hit or wounds
    cover = False # True/False if target has cover
     
    
    attack_results_df = pd.DataFrame()
    weapon_df = pd.DataFrame.from_dict(weapon_profile)

    for index, row in weapon_df.iterrows():
           
        num_dice = num_attacks * weapon_df['Attacks'][index]
        
        roll_results = roll_dice(num_dice)
        #print('roll result', roll_results)
            
        attack_dict =({"Name": weapon_df["Name"][index],
                       "Attack Roll Results": roll_results,
                       })

        #3print('attack dict', attack_dict)
        attack_df =  pd.DataFrame.from_dict(attack_dict)
        #print('attack df', attack_df)

        attack_results_df =  pd.concat([attack_results_df,attack_df])
        #print('attack_results_df',attack_results_df)
    
    
    
    
    calc_results(attack_results_df,weapon_df)

    
def roll_dice(num_dice):
    
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_results


def calc_results(attack_results_df,weapon_df):
    
    hits_results_df = pd.DataFrame()
    
    count_sr = attack_results_df.groupby(['Name', 'Attack Roll Results']).size()#.groupby(level=0).max()

    count_df = pd.DataFrame(count_sr).reset_index()
    count_df.columns.values[2] = "counts"
    print(count_df)
    print(count_df.shape)
    
    for index, row in weapon_df.iterrows():
        
        Success_hit = count_df.loc[(count_df['Name'] ==  weapon_df["Name"][index]) & 
                                   ( count_df['Attack Roll Results'] >= weapon_df['Weapon Skill'][index]), 'counts'].sum()
        
        #add crits
        crit_hit = count_df.loc[(count_df['Name'] ==  weapon_df["Name"][index]) & 
                                   ( count_df['Attack Roll Results'] >= weapon_df['Crits'][index]), 'counts'].sum()
        
        Results_dict =({"Name": weapon_df["Name"][index],
                       "Num of hits": [Success_hit],
                       "Num of crits": [crit_hit],
                       })
        
        #print("Results",Results_dict)
        hits_df =  pd.DataFrame.from_dict(Results_dict)
        #print('hits df', hits_df)
        hits_results_df =  pd.concat([hits_results_df,hits_df])
        
    
    
    print('hit results',hits_results_df)
    #display(hits_results_df)


if __name__ == "__main__":
    main()
