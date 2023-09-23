import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

data = pd.read_csv("dataFiles/startups1.csv")
# print(data)

X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

ct = ColumnTransformer(transformers= [('encode', OneHotEncoder(), [3])], remainder='passthrough')
X = ct.fit_transform(X)
X = X[:,1:]
# print(X)

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
# print(x_train)
# print()
# print(y_train)
# print()
# print(x_test)
# print()
# print(y_test)

regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)
print(r2_score(y_test, y_pred))