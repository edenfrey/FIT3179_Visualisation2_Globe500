from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://www.bloomberg.com/billionaires/'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
time.sleep(3)

soup = BeautifulSoup(driver.page_source,'html5lib')

names = [name.text.strip() for name in soup.find_all('div', class_ = 'table-cell t-name')]

net_worth = [nw.text.strip() for nw in soup.find_all('div', class_ = 'table-cell active t-nw')]
net_worth = [x[1:-1] for x in net_worth]

country = [country.text.strip() for country in soup.find_all('div', class_ = 'table-cell t-country')]

industry = [industry.text.strip() for industry in soup.find_all('div', class_ = 'table-cell t-industry')]

print(names)
print(net_worth)
print(country)
print(industry)

df = pd.DataFrame([names,net_worth,country,industry]).T
df.columns=['Name','Net Worth','Country','Industry']
df['Net Worth'] = df['Net Worth'].shift(-1)
df['Country'] = df['Country'].shift(-1)
df['Industry'] = df['Industry'].shift(-1)

df.to_csv("Billionaires_October_13_2022.csv", index = False)