import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

def load_and_process():
    
    df = (
        pd.read_csv('C:/Users/adamv/Documents/mgmt301/Project/project-group-group-57/data/raw/MutualFunds.csv')
        .assign(Standard_Deviation=lambda x: x.iloc[:, 56:67].std(axis=1, numeric_only=True),
                Mean=lambda x: x.iloc[:, 56:67].mean(axis=1, numeric_only=True))
        .loc[:, ['fund_symbol', 'fund_long_name', 'fund_sector_basic_materials', 'fund_sector_communication_services',
                 'fund_sector_consumer_cyclical', 'fund_sector_consumer_defensive', 'fund_sector_energy',
                 'fund_sector_financial_services', 'fund_sector_healthcare', 'fund_sector_industrials',
                 'fund_sector_real_estate', 'fund_sector_technology', 'fund_sector_utilities', 'Standard_Deviation',
                 'Mean', 'fund_return_ytd', 'fund_return_1month', 'fund_return_3months', 'fund_return_1year',
                 'fund_return_3years', 'fund_return_5years']]
        .dropna()
    )
    
    return df