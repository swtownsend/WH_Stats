import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def create_bargraph(weapon_df,hit_results_df,wounds_results_df,save_results_df ):

    hit_results_df.plot(x="Name", rot=0 ,title="Num of successful hits by Weapon", kind='bar')

    wounds_results_df.plot(x="Name",rot=0, title="Num of successful Wounds by Weapon",kind='bar')

    save_results_df.plot(x="Name",rot=0, title="Amt of damage by Weapon",kind='bar')

    dmg_2v_df = save_results_df[['Name',"Save 2+ vs Wound 2+","Dmg 2v2","Save 3+ vs Wound 2+","Dmg 3v2",
                                 "Save 4+ vs Wound 2+","Dmg 4v2","Save 4+ vs Wound 2+","Dmg 5v2","Save 6+ vs Wound 2+",
                                 "Dmg 6v2","Dev Wounds","Dev Wounds Dmg"]].copy()

    print(dmg_2v_df)
    dmg_2v_df.plot(x="Name", rot=0, title="Amt of damage by Weapon(Invuln saves wounding on 2+)", kind='bar')

    plt.show()