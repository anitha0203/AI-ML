import pandas as pd


drinks = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/drinks.csv')
print(drinks.head())

print(drinks.drop('continent', axis=1).head())

print(drinks.drop(1, axis=0).head())

# print(drinks.mean(axis=0))
# print(drinks.mean(axis='index'))
print()
numeric_columns = drinks.select_dtypes(include='number')
print()
print(numeric_columns.mean(axis=0))
print()
print(numeric_columns.mean(axis='index'))
print()
print(numeric_columns.mean(axis=1))
print()
print(numeric_columns.mean(axis='columns'))
# print(drinks.mean(axis=1))
# print(drinks.mean(axis='column'))



############################################################################################################### 11


orders = pd.read_table('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/chipotle.tsv')
print(orders.item_name.str.upper())

print(orders[orders.item_name.str.contains('Chicken')])





############################################################################################################### 12



drinks = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/drinks.csv')

print(drinks.head())
print(drinks.dtypes)
 
drinks['beer_servings'] = drinks['beer_servings'].astype(float)
print(drinks.dtypes)




drinks1 = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/drinks.csv', dtype={'beer_serving':float})
print(drinks1)




orders = pd.read_table('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/chipotle.tsv')

print(orders.item_price.str.replace('$', '').astype(float).mean())




############################################################################################################### 13

import matplotlib.pyplot as plt

drinks1 = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/drinks.csv')

print(drinks1.groupby('continent').beer_servings.mean())

print(drinks1[drinks1.continent == 'Europe'].beer_servings.mean())

print(drinks1.groupby('continent').beer_servings.agg(['count', 'min', 'max', 'mean']))


numeric_columns = drinks1.select_dtypes(include='number')
numeric_columns['continent'] = drinks1['continent']
mean_by_continent = numeric_columns.groupby('continent').mean()
print(mean_by_continent)

numeric_columns.groupby('continent').mean().plot(kind='bar')
plt.show()



############################################################################################################### 14


movies = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv')

movies.duration.plot(kind='hist')
plt.show()


movies.genre.value_counts().plot(kind='bar')
plt.show()



############################################################################################################### 15


ufo = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv', sep=',')

print(ufo.tail())




############################################################################################################### 16


drinks = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/drinks.csv')

print(drinks.head())

print(drinks.index)

print(drinks[drinks.continent == 'South America'])


drinks.set_index('country', inplace=True)
print(drinks.head())

drinks.index.name = None
print(drinks.head())




############################################################################################################### 17


drinks = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/drinks.csv')

print(drinks.continent.value_counts())

print(drinks.continent.value_counts().values)

print(drinks.continent.value_counts()['Africa'])

print(drinks.continent.value_counts().sort_values())

print(drinks.continent.value_counts().sort_index)

people = pd.Series([3000000, 85000], index=['Albania', 'Andorra'], name='population')
print(people)

print(pd.concat([drinks, people], axis=1).head())




############################################################################################################### 18


ufo = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv', sep=',')

print(ufo.head())

print(ufo.loc[0, :])

print(ufo.loc[[0, 1, 2], :])

print(ufo.loc[0:2, :])

print(ufo.loc[0:2])

print(ufo.loc[:, 'City'])

print(ufo.loc[:, 'City':'State'])


print(ufo.iloc[:, 0:3])



########        deprecated      ###############

# drinks = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/drinks.csv', index_col='country')

# print(drinks.ix['Albania', 0])

# print(drinks.ix[1, 'beer_servings'])

# print(drinks.ix['Albania':'Andorra', 0:2])



############################################################################################################### 19


ufo = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv', sep=',')

print(ufo.drop('City', axis=1, inplace=True))

print(ufo)
print(ufo.dropna(how='any'))


ufo.set_index('Time', inplace=True)
ufo = ufo.set_index('Time')
print(ufo.tail())




############################################################################################################### 20
