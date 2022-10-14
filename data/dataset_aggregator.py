import pandas as pd
import numpy as np
data = pd.read_csv('data\Billionaires_October_13_2022.csv')
data.info()

"""
# Get country and amount of billionaires.
country_count = data['Country'].value_counts()
country_count.columns = ['Count']
country_count.to_csv('data\Billionaire_Count_by_Country.csv', sep = ',', encoding ='utf-8')
"""
"""
# country_totall_mean_networth
result_mean = data.groupby('Country')['Net Worth'].mean().sort_values(ascending=False)
print(result_mean)

result_sum = data.groupby('Country')['Net Worth'].sum().sort_values(ascending=False)
print(result_sum)

merged_inner = pd.merge(left=result_sum, right=result_mean, left_on='Country', right_on='Country')
merged_inner.columns = ['Total', 'Mean']
print(merged_inner)
merged_inner.to_csv('data\Country_Average_Total.csv', sep = ',', encoding ='utf-8')
"""
"""
# Industry_Total_Mean
result_mean = data.groupby('Industry')['Net Worth'].mean().sort_values(ascending=False)
print(result_mean)

result_sum = data.groupby('Industry')['Net Worth'].sum().sort_values(ascending=False)
print(result_sum)

merged_inner = pd.merge(left=result_sum, right=result_mean, left_on='Industry', right_on='Industry')
merged_inner.columns = ['Total', 'Mean']
print(merged_inner)
merged_inner.to_csv('data\Industry_Average_Total.csv', sep = ',', encoding ='utf-8')
"""

