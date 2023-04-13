import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns


def load_and_process():
    
    df = (
        pd.read_csv('/Users/georgehsu/project-group-group-57/data/raw/MutualFunds.csv')
        .assign(Standard_Deviation=lambda x: x.iloc[:, 56:67].std(axis=1, numeric_only=True),
                Mean=lambda x: x.iloc[:, 56:67].mean(axis=1, numeric_only=True),
                fund_sector_differentiation=lambda x: np.where(x['Mean'] < 0.29697 , 'Low', 
                                                               np.where(x['Mean'] > 0.10640, 'High', 
                                                                        'Moderate')))
        .loc[:, ['fund_symbol', 'fund_return_2021_q2', 'fund_return_2021_q1', 'fund_return_2020_q4', 
                  'fund_return_2020_q3', 'fund_return_2020_q2', 'category_return_2020', 'fund_return_2020']]
        .dropna()
        
    )
    
    return df