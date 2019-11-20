import sklearn as sci
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

train = pd.read_csv('train.csv')
building_metadata = pd.read_csv('building_metadata.csv')
weather_train = pd.read_csv('weather_train.csv')

A = pd.to_datetime(train['timestamp'],format='%Y-%m-%d %H:%M:%S')
train['timestamps'] = A

dfObj = pd.DataFrame()
site_id=[]
primary_use=[]
square_feet=[]
year_built=[]
floor_count=[]

for i in train.index:
    print(i)
#    dfObj.append(building_metadata.iloc[train['building_id'][i]])
    site_id.append(building_metadata['site_id'][ train['building_id'][i]])
    primary_use.append(building_metadata['primary_use'][ train['building_id'][i]])
    square_feet.append(building_metadata['square_feet'][ train['building_id'][i]])
    year_built.append(building_metadata['year_built'][ train['building_id'][i]])
    floor_count.append(building_metadata['floor_count'][ train['building_id'][i]])

train['site_id']= site_id
train['primary_use']=primary_use
train['square_feet']=square_feet
train['year_built']=year_built
train['floor_count']=floor_count

del train['building_id']        
