import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def create_bargraph(weapon_df, hit_results_df, wounds_results_df, save_results_df):
    avg_hit_results_df = hit_results_df.groupby(["Name"]).mean()
    avg_hit_results_df.reset_index(inplace=True)
    #avg_hit_results_df.plot(x="Name", rot=0, title="Avg of successful hits by Weapon", kind='bar')

    avg_wounds_results_df = wounds_results_df.groupby(["Name"]).mean()
    avg_wounds_results_df.reset_index(inplace=True)
    #avg_wounds_results_df.plot(x="Name", rot=0, title="Avg of successful Wounds by Weapon", kind='bar')

    avg_save_results_df = save_results_df.groupby(['Name']).mean()
    avg_save_results_df.reset_index(inplace=True)
    #avg_save_results_df.plot(x="Name", rot=0, title="Avg Amt of damage by Weapon", kind='bar')



def create_attack_wnd_percent(weapon_df, hit_results_df, wounds_results_df, save_results_df):
    attack_wnd_df = pd.DataFrame()
    avg_hit_results_df = hit_results_df.groupby(["Name"]).mean()
    avg_hit_results_df.reset_index(inplace=True)
    avg_wounds_results_df = wounds_results_df.groupby(["Name"]).mean()
    avg_wounds_results_df.reset_index(inplace=True)
    avg_save_results_df = save_results_df.groupby(['Name']).mean()
    avg_save_results_df.reset_index(inplace=True)

    #attack_wnd_df = weapon_df.copy()


    #save_results_df['Total attacks'] = hit_results_df['Total attacks']

    sns.lmplot(x='Amt of Dmg',y="Num of Successful Saves",hue='Name', data=save_results_df)

    #attack_wnd_df.plot(x='Name')
    plt.show()


def merge_data(save_results_df):
    pd.set_option('display.max_columns', None)
    print(save_results_df.shape)
    print(save_results_df.head)
    print(save_results_df.tail)

    #sns.lmplot(x='Total Attacks',y="Amt of Dmg", data=save_results_df)
    sns.lmplot(y='Amt of Dmg',x="Num of Hits",hue='Name', data=save_results_df)
    
    #attack_wnd_df.plot(x='Name')
    plt.show()





