"""
import numpy as np
i2=[9, 22, 51, 1829, 2981, 5817, 5818]
i1=[8, 10, 23, 52, 1830, 2982, 5818, 5819, 5820]
dict1={"file1":i1}
dict2={"file2":i2}
def checkreturn(di1,di2):
    
    a=np.asarray(list(di1.values())[0])
    b=np.asarray(list(di2.values())[0])
    
    checka=[]
    i=0
    while(len(a)>0 and len(b)>0 ):
        print("a:", a)
        print("b:", b)
        if(a[0] in b):
            checka.append("Unmatch")
            a=np.delete(a,0)
            b=np.delete(b,0)
        else:
            if(a[0]<b[0]):
                checka.append("Not found {}".format(str(di2.keys())[-8:-2]))
                a=np.delete(a,0)
                a=a-1
            else:
                #checka.append("Not found {}".format(str(di1.keys())[-8:-2]))
                b=np.delete(b,0)
                a=a+1
    if(len(a)>0):
        for i in range(0,len(a))  :
            checka.append("Not found {}".format(str(di2.keys())[-8:-2])) 
    return checka              

print(checkreturn(dict1,dict2))        

"""
import config
import numpy as np 
import pandas as pd
import csv
from reading import read_dat
import os
import sys,glob
import time           


def checkreturn(di1,di2):        
        a=np.asarray(list(di1.values())[0])
        b=np.asarray(list(di2.values())[0])        
        checka=[]
        checkb=[]
        while(len(a)>0 and len(b)>0 ):            
            if(a[0] in b):
                checka.append("Unmatch")
                checkb.append("Unmatch")
                a=np.delete(a,0)
                b=np.delete(b,0)
            else:
                if(a[0]<b[0]):
                    checka.append("Not found {}".format(str(di2.keys())[-8:-2]))
                    a=np.delete(a,0)
                    a=a-1
                else:
                    checkb.append("Not found {}".format(str(di1.keys())[-8:-2]))
                    b=np.delete(b,0)
                    a=a+1
        if(len(a)>0):
            for i in range(0,len(a))  :
                checka.append("Not found {}".format(str(di2.keys())[-8:-2])) 
        return checka 
def matchresult(df,index,returnfai):
        result1=[]
        for i in range(0,len(df)):  
            if i not in index: 
                result1.append("Match")
            else:                
                result1.append(returnfai[index.index(i)])
        return result1
file= sys.path[0][0:-11]+'testdata/shclog.xlsx'
file1= sys.path[0][0:-11]+'testdata/shclogcopy.xlsx'
df1= pd.read_excel(file,na_values=['NA'])
df2= pd.read_excel(file1,na_values=['NA'])
df=pd.merge(df1, df2, how='inner')
df3=pd.concat([df,df1]).drop_duplicates(keep=False)
df4=pd.concat([df,df2]).drop_duplicates(keep=False)
index1=list(df3.index)
index2=list(df4.index)
ind=sorted(np.unique(index1+index2))
if(len(df1)<len(df2)):
    df=df2
else:
    df=df1
check=[]
i1=index1
i2=index2
dict1={"Napas":i1}
dict2={"FPT":i2}    
returnfail1=checkreturn(dict1,dict2)
returnfail2=checkreturn(dict2,dict1)   

result1=matchresult(df1,index1,returnfail1)
result2=matchresult(df2,index2,returnfail2)
df1["Check"]=result1
df1.to_excel(sys.path[0][0:-11]+'testdata/result/result1.xlsx')
df2["Check"]=result2
df2.to_excel(sys.path[0][0:-11]+'testdata/result2.xlsx')

print(result1)

"""
matchnum=sum(map(lambda x : x == "Match", result1))
unmatchnum=sum(map(lambda x : x == "Unmatch", result1))
notfoundnum=sum(map(lambda x : x == "Not found file1", result1))
print(matchnum,unmatchnum,notfoundnum)
res={
    "Match":matchnum,
    "Unmatch":unmatchnum,
    "Notfound in 1":notfoundnum
}
print(res)
"""
