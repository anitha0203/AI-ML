import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import seaborn as sns

data = pd.read_csv("dataFiles/salaries.csv")
# print(data)
# print(data.isna().sum())

X = data.iloc[:, 1:-1].values
y = data.iloc[:, -1].values

print(X)
print(y)
# sns.pairplot(data)
# plt.show()

poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)

lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

plt.scatter(X, y, color="red")
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color= "blue")
plt.xlabel('Position Level')
plt.ylabel('Salary') 
plt.show()

p_salary = lin_reg_2.predict(poly_reg.fit_transform([[2.5]]))
print(p_salary)