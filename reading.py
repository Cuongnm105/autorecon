import numpy as np 
import csv
import pandas as pd
import config
# read flash.dat to a list of lists
class read_dat():
    def __init__(self,filename) -> None:
        self.name=filename
    def create_line(data):
        data_n=[]        
        for i in range(0,len(data)):
            d=[]
            dat=data[i].split("]")
            for da in dat:
                d1=da.split("[")        
                d.append(d1[0])
            data_n.append(d)
        return data_n

    def readbody(self):
        with open(self.name, 'r') as fin:
            data = fin.read().splitlines(True)
            data_new=data[1:-1]
        label=config.label
        data_new=read_dat.create_line(data_new)
        tab=pd.DataFrame(data_new,columns=label)
        
        return tab
a=read_dat('091421_ISS_DOB_970406_1_TC_SWC.dat')
a.readbody().to_excel("ouput.xlsx")



