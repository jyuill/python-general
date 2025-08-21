# pandas tutorial
# from Tech with Tim, YT, Aug, 2025
# https://www.youtube.com/watch?v=EXIgjIBu4EU&t=21s

import pandas as pd

# 3 main options for data frames

# 1. from a data dictionary
# 2. from a csv file
# 3. from a excel filelist

# 1. create a dataframe from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Reggie'],
    'Age': [25, 30, 35, 28],
    'City': ['Vancouver', 'Calgary', 'Edmonton', 'Toronto']
}
# convert to dataframe
my_df = pd.DataFrame(data)
print(my_df)

# save to csv
my_df.to_csv('my_df.csv', index=False)

# 2. import csv - random csv added to repo
df = pd.read_csv('exp_cats_gpt.csv')
print(df.head())

# 3. import excel - random excel added to repo
df_excel = pd.read_excel('expenses.xlsx', 
            sheet_name = 'expenses_01', 
            skiprows=2) # (skip first 2 rows)
print(df_excel.head())

