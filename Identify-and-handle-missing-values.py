import pandas as pd

df = pd.read_csv('diabetes.csv')

missing_data = df.isnull()
print(missing_data.head(2))

for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")