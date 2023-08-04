import pandas as pd


ufo = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv')


print(ufo.shape)

print(ufo.drop_duplicates(keep='first').shape)

print(ufo.drop_duplicates(keep='last').shape)

print(ufo.drop_duplicates(keep=False).shape)



############################################################################################################### 26

import numpy as np

movies = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv')

movies.loc[movies.content_rating == 'NOT RATED', 'content_rating'] = np.nan

print(movies)

print(movies.content_rating.isnull().sum())



############################################################################################################### 27

# data = pd.Series([10020, 23039, 20000, 239000])

# data = pd.set_option('display.float_format', '{:,}'.format)

# print(data)

import pandas as pd

data = pd.Series([100, 2000, 10020, 230039, 2390500])

# Format the numbers with commas as thousands separators
data_formatted = data.apply('{:,}'.format)

print(data_formatted)





############################################################################################################### 28







############################################################################################################### 29







############################################################################################################### 30