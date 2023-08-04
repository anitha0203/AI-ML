import pandas as pd


data = pd.read_table('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/chipotle.tsv')
print(data.head())




movie = pd.read_table('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/u.user', sep='|')

movie_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
movie1 = pd.read_table('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/u.user', sep='|', header=None, names=movie_cols)
print(movie1.head())




############################################################################################################### 2


ports = pd.read_table('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv', sep=',')

print(type(ports))
print(ports.head())






############################################################################################################### 3


ratings = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv')

# print(ratings.head())


print(ratings.describe())
print(ratings.shape)

 





############################################################################################################### 4


ports = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv')

print(ports.columns)
ports.rename(columns = {'Colors Reported':'Colors_Reported'}, inplace = True)
print(ports.head())

#               ORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR

cols = ['city', 'colors', 'shape', 'state', 'time']
ports.columns = cols
print(ports.head())

'''

ports.columns = ports.columns.str.replace(' ', '_')
print(ports.columns)

'''






############################################################################################################### 5


ports = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv')

#                   columns
ports.drop('Colors Reported', axis=1, inplace = True)
#   ORR
# ports.drop(['Colors Reported', 'City'], axis=1, inplace = True)
print(ports.head())


#                   rows
ports.drop([0, 1], axis=0, inplace = True)
#   ORR
# ports.drop(['0', '1'], inplace = True)
print(ports.head())


############################################################################################################### 6


ratings = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv')

print(ratings.title.sort_values())
# print(ratings['title']sort_values())


print(ratings.title.sort_values(ascending=False))






print(ratings.sort_values('title',ascending=False))

print(ratings.sort_values(['title', 'duration']))


############################################################################################################### 7



ratings = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv')

booleans = []

for length in ratings.duration:
    if length >= 200:
        booleans.append(True)
    else:
        booleans.append(False)

print(booleans[0:5])
print(len(booleans))

is_long = pd.Series(booleans)
print(is_long.head())

print(ratings[is_long])



print(ratings[ratings.duration >= 200])
print(ratings[ratings.duration >= 200]['genre'])
print(ratings.loc[ratings.duration >= 200, 'genre'])




############################################################################################################### 8



ratings = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv')

print(ratings[(ratings.duration >= 200) & (ratings.genre == 'Drama')])


print(ratings[(ratings.duration >= 200) | (ratings.genre == 'Drama')])

print(ratings.genre.isin(['Crime', 'Drama', 'Action']))





############################################################################################################### 9


# ratings = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv', usecols=['City', 'State'])
# print(ratings)

ratings1 = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv', usecols=[0, 4])
print(ratings1)



ratings1 = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv', nrows=4)
print(ratings1)


print("\n\n")
drinks = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/drinks.csv')

import numpy as np

print(drinks.select_dtypes(include=[np.number]).dtypes)




############################################################################################################### 10
