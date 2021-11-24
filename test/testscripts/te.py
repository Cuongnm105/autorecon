from os import truncate
import pandas as pd
import numpy as np
import sys
import time
start=time.time()
file= sys.path[0][0:-11]+'testdata/ouput.xlsx'
file1= sys.path[0][0:-11]+'testdata/ouput_Copy.xlsx'
df1= pd.read_excel(file,na_values=['NA'])
df2= pd.read_excel(file1,na_values=['NA'])

#df3=pd.concat([df2,df1]).drop_duplicates(keep=False)
df=pd.merge(df1, df2, how='inner')


#dfx=pd.merge(df1, df2, how='outer')



df3=pd.concat([df,df1]).drop_duplicates(keep=False)
df4=pd.concat([df,df2]).drop_duplicates(keep=False)
df5=pd.concat([df1,df2]).drop_duplicates(keep=False)
print(pd.merge(df1,df2,how='outer',indicator=True).to_excel("hhh.xlsx"))
index1=list(df3.index)

index2=list(df4.index)

print(index1)
print(index2)
checka=[]
for i in range(0,len(index1)):
    a=[]
    print("i=",i,index1[i])
    for j in range(0,len(index2)):
        print("j=",j,index2[j])
        a.append(len(df1.loc[index1[i]].compare(df2.loc[index2[j]])))

    print(min(a))
    if(min(a)<8):
        checka.append("Unmatch") 
    else:
        checka.append("notfoundin2") 
print(checka)