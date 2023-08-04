import pandas as pd

####################################################################################################################


print("Empty Cells")

#   the dropna() method returns a new DataFrame, and will not change the original.
df = pd.read_csv('data1.csv')
new_df = df.dropna()
print(new_df.to_string())


print()
#   the dropna(inplace = True) will NOT return a new DataFrame, 
#   but it will remove all rows containing NULL values from the original DataFrame.
df.dropna(inplace = True)
print(df.to_string())


#   the dropna() method returns a new DataFrame, and will not change the original.

df = pd.read_csv('data1.csv')
df.fillna(130, inplace = True)
print(df)

df = pd.read_csv('data1.csv')
df["Calories"].fillna(130, inplace = True)
print(df.to_string())





# A common way to replace empty cells, is to calculate the mean, median or mode value of the column.
# Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:

#   Mean = the average value (the sum of all values divided by number of values).
df = pd.read_csv('data1.csv')
x = df["Calories"].mean()
df["Calories"].fillna(x, inplace = True)
print(df)


#   Median = the value in the middle, after you have sorted all values ascending.
df = pd.read_csv('data1.csv')
x = df["Calories"].median()
df["Calories"].fillna(x, inplace = True)
print(df)


#   Mode = the value that appears most frequently.
df = pd.read_csv('data1.csv')
x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace = True)
print(df)


####################################################################################################################


print("Wrong Format")


# df = pd.read_csv('data1.csv')
# df['Date'] = pd.to_datetime(df['Date'])
# print(df.to_string())



df = pd.read_csv('data1.csv')
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
print(df.to_string())


df = pd.read_csv('data1.csv')
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
df.dropna(subset=['Date'], inplace = True)
print(df.to_string())




####################################################################################################################


print("Wrong Data")

df = pd.read_csv('data1.csv')
df.loc[7,'Duration'] = 45
print(df.to_string())


df = pd.read_csv('data1.csv')

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120
print(df.to_string())


df = pd.read_csv('data1.csv')
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)
#remember to include the 'inplace = True' argument to make the changes in the original DataFrame object instead of returning a copy

print(df.to_string())



####################################################################################################################


print("Duplicates")


df = pd.read_csv('data1.csv')
print(df.duplicated())

df.drop_duplicates(inplace = True)
print(df.to_string())


####################################################################################################################