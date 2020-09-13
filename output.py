import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
 
df = pd.read_excel('results.xlsx', sheetname='Sheet1')
print("Column headings:")
print(df.columns[0])
print(df.columns[1])
print(df.columns[2])
print(df.columns[3])
print(df.columns[4])
print(df.columns[5])
a = df.columns[0]
print(type(a))