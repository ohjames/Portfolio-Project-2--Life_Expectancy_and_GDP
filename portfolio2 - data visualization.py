import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv('all_data.csv')
print(df.head())

print(df.Country.unique())
print(df.Year.unique())
#rename life expectancy column
df = df.rename({'Life expectancy at birth (years)': 'Life_Expectancy'}, axis = 'columns')

chile_year = df.Year[df.Country == 'Chile']
china_year = df.Year[df.Country == 'China']
germany_year = df.Year[df.Country == 'Germany']
mexico_year = df.Year[df.Country == 'Mexico']
usa_year = df.Year[df.Country == 'United States of America']
zimbabwe_year = df.Year[df.Country == 'Zimbabwe']

#Has life expectancy increased over time in the six nations?
plt.figure(figsize=(8,6))
sns.lineplot(x = df.Year, y = df.Life_Expectancy, hue = df.Country)
plt.legend()
plt.ylabel('Life expectancy at birth (years)')
plt.show()
plt.clf()
#Has GDP increased over time in the six nations?
plt.figure(figsize=(8,6))
sns.lineplot(x = df.Year, y = df.GDP, hue = df.Country)
plt.legend()
plt.ylabel('GDP in Trillions of USD')
plt.show()
plt.clf()
#Is there a correlation between GDP and life expectancy of a country?
plt.figure(figsize=(8,6))
sns.scatterplot(x = df.Life_Expectancy, y = df.GDP, hue = df.Country)
plt.legend()
plt.xlabel('Life expectancy at birth (years)')
plt.ylabel('GDP in Trillions of USD')
plt.show()
plt.clf()
#What is the average life expectancy in these nations?
dfMeans = df.drop('Year', axis = 1).groupby('Country').mean().reset_index()
plt.figure(figsize=(8,6))
sns.barplot(x = 'Life_Expectancy', y = 'Country', data = dfMeans)
plt.xlabel('Life expectancy at birth (years)')
plt.show()
plt.clf()
#What is the distribution of life expectancy?
plt.figure(figsize=(8,6))
sns.displot(df.Life_Expectancy, rug = True, kde = False)
plt.xlabel('Life expectancy at birth(years)')
plt.show()
plt.clf()