import pandas as pd
import numpy as np

data = pd.read_csv("dataFiles/languages.csv")
# print(data)

X = data.iloc[: , :-1].values
# print(X)

y = data.iloc[: , -1].values
# print(y)

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='median')
X[: , 1:4] = imputer.fit_transform(X[: , 1:4])

# print(X)

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer


ct = ColumnTransformer(transformers= [('encode', OneHotEncoder(), [0])], remainder='passthrough')
X = ct.fit_transform(X)

# print(X)

X = X[:, 1:]

# print(X)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# print(x_train)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

print(x_train)