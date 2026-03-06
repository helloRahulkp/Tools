import pandas as pd

df = pd.read_csv("diabetes.csv")
print(df.head(5))

print(df.shape)

print(df.info())

print(df.describe())