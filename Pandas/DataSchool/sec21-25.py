import pandas as pd


drinks = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/drinks.csv')
print(drinks.head())

print(drinks.memory_usage(deep=True))

print(sorted(drinks.continent.unique())) 



############################################################################################################### 21


train = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/titanic_train.csv')

print(train.head())

feature_cols = ['Pclass', 'Parch']

X = train.loc[:, feature_cols]
print(X.shape)

Y = train.Survived
print(Y.shape)


from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()
logreg.fit(X, Y)

test = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/titanic_train.csv')

print(test.head())


X1 = test.loc[:, feature_cols]
print(X1.shape)

# new_pred = logreg.predict(X1)
# print(test.passengerId)



############################################################################################################### 22





############################################################################################################### 23


train = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/titanic_train.csv')

print(pd.get_dummies(train.Embarked, prefix='Embraked'))

embraked_dummies = pd.get_dummies(train.Embarked, prefix='Embraked').iloc[:, 1:]

print(embraked_dummies)




############################################################################################################### 24


ufo = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv')

print(ufo.dtypes)

print(ufo.Time.str.slice(-5, -3).astype(int).head())

ufo['Time'] = pd.to_datetime(ufo.Time)
print(ufo.head())




############################################################################################################### 25