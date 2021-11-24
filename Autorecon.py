import pandas as pd
import numpy as np
import sys

file= sys.path[0][0:-11]+'testdata/ouput.xlsx'
file1= sys.path[0][0:-11]+'testdata/ouput_copy.xlsx'
df1= pd.read_excel(file,'Sheet1',na_values=['NA'])
df2= pd.read_excel(file1,'Sheet1',na_values=['NA'])
df3=pd.concat([df2,df1]).drop_duplicates(keep=False)
dfx=pd.concat([df1,df],axis=1)

print(dfx)

df4 = df2[df1.ne(df2).any(axis=1)]
print(df4)

df5 = df1[df2.ne(df1).any(axis=1)]
print(df5)
