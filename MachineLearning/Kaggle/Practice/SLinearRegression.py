import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

data = pd.read_csv("dataFiles/employees.csv")
# print(data)

X = data.iloc[:, :1].values
# print(X)
y = data.iloc[:, -1].values
# print()
# print(y)

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

plt.scatter(x_train, y_train, color="red")
plt.plot(x_train, regressor.predict(x_train), color= "blue")
plt.xlabel('Experience')
plt.ylabel('Years')
plt.show()

plt.scatter(x_test, y_test, color="red")
plt.plot(x_test, regressor.predict(x_test), color= "blue")
plt.xlabel('Experience')
plt.ylabel('Years')
plt.show()