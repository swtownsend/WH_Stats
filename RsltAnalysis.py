import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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


def merge_data(weapon_df, hit_results_df, wounds_results_df, save_results_df):

    for index, row in weapon_df.iterrows():

        print(save_results_df['Wound Roll'][index] == wounds_results_df['Wound Roll'][index])
        print(save_results_df["Name"][index] == wounds_results_df['Name'][index])

        if ((save_results_df['Wound Roll'][index].astype(int) == wounds_results_df['Wound Roll'][index].astype(int)) &
                (save_results_df["Name"][index] == wounds_results_df['Name'][index])):
            save_results_df['Num Successful Wounds'][index] = wounds_results_df['Wound Roll'][index]


    print(save_results_df.shape)
    print(save_results_df.head)
    print(save_results_df.tail())


