import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns


def process_data(file_path1, file_path2, start_date=2000):
    data1 = pd.read_csv(file_path1)
    unique_fund_symbols = data1.groupby('fund_family')['fund_symbol'].first().reset_index()
    filtered_data = data1.merge(unique_fund_symbols, on=['fund_family', 'fund_symbol'])
    year_columns = [col for col in filtered_data.columns if col.startswith('fund_return_')]

    df_melted = (filtered_data.melt(id_vars=['fund_symbol'], value_vars=year_columns, var_name='Year', value_name='Value')
                 .assign(Year=lambda x: x['Year'].str.extract('(\d{4})'),
                         Date=lambda x: pd.to_datetime(x['Year'], format='%Y') + pd.offsets.MonthBegin(1),
                         Value=lambda x: x['Value'] * 100)
                 .sort_values(['fund_symbol', 'Year'])
                 .assign(cumulative_value=lambda x: x.groupby('fund_symbol')['Value'].cumsum())
                )

    data2 = pd.read_csv(file_path2)
    data2f = (data2.loc[data2['year'] >= start_date]
              .reset_index(drop=True)
              .assign(fund_symbol='S&P500',
                      cumulative_value=lambda x: x[' value'].cumsum())
              .rename(columns={'year': 'Year', 'date': 'Date', ' value': 'Value'})
             )

    merged_df = pd.concat([df_melted, data2f], ignore_index=True)
    
    return merged_df

file_path1 = '../data/processed/MutualFund'
file_path2 = '../data/processed/S&P'
result_df = process_data(file_path1, file_path2)
result_df.to_csv('../data/processed/S&P2 and Mutual', index=True)
result_df