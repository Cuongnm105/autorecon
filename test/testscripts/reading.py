import numpy as np 
import csv
import pandas as pd
import config
class read_dat():
    def __init__(self,filename) -> None:
        self.name=filename
    def create_line(data):
        data_n=[]        
        for i in range(0,len(data)):
            data_line=[]
            data_split=data[i].split("]")
            for da in data_split:
                data_split1=da.split("[")        
                data_line.append(data_split1[0])
            data_n.append(data_line)
        return data_n

    def readbody(self):
        with open(self.name, 'r') as fin:
            data = fin.read().splitlines(True)
            data_new=data[1:-1]
        label=config.label
        data_new=read_dat.create_line(data_new)
        tab=pd.DataFrame(data_new,columns=label)
        
        return tab



