import pandas as pd
data = pd.read_csv('data\Billionaires_October_13_2022.csv')
data.info()
"""
country_count = data['Country'].value_counts()
country_count.columns = ['Country','Count']
country_count.to_csv('data\Billionaire_Count_by_Country.csv', sep = ',', encoding ='utf-8')
"""

