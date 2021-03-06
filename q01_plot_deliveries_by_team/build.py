import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_deliveries_by_team():
    val=ipl_df.groupby('batting_team')
    final=val['delivery'].count()
    final.plot(kind='bar')
    plt.show()
