import pandas as pd

print(pd.__version__)

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
# print(mydataset)
myvar = pd.DataFrame(mydataset)
print("\nDataFrame")
print(myvar)



a = [1, 7, 2]
myvar = pd.Series(a)
print("\nSeries")
print(myvar)


print("\nWith the index argument, you can name your own labels.")
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)


print("\nCreate a simple Pandas Series from a dictionary.")
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
#load data into a DataFrame object:
df = pd.DataFrame(data)
print()
print(df.loc[0])
print()
print(df.loc[[0, 1]], "\n")

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df) 
print()
print(df.loc["day1"])



df = pd.read_csv('data.csv')
print(df.to_string()) 
print(df) 



print(pd.options.display.max_rows)

pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')
print(df.head())          #       top 5 rows
print(df.head(10))        #       top 10 rows

print(df.tail())          #       bottom 5 rows
print(df.tail(10))        #       bottom 10 rows

print("\n\n")
print(df.info())          #       that gives you more information about the data set


print("\njson data\n")
df = pd.read_json('data.json')
# print(df.to_string()) 