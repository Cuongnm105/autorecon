import config
import numpy as np 
import pandas
import csv
from reading import read_dat
a=read_dat('091421_ISS_DOB_970406_1_TC_SWC.dat')
a.readbody().to_excel("ouput.xlsx")