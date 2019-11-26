import sklearn as sci
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

ds = pd.read_csv('train_inncomplete.csv')
weather_train = pd.read_csv('weather_train.csv')
ds = ds.values

a = np.empty((20216100,2))
a[:] = np.nan
ds = np.hstack((ds,a))
 
a = np.empty((139773,3))
a[:] = np.nan
weather_train = np.hstack((weather_train,a))
H=[]
D=[]
M=[]
for i in range(len(weather_train[:,1])):
    h=float(weather_train[:,1][i][11:13])
    d=float(weather_train[:,1][i][8:10])
    m=float(weather_train[:,1][i][5:7])
    H.append(h)
    D.append(d)
    M.append(m)
H=np.array(H)
D=np.array(D)
M=np.array(M)

weather_train[:,9]=H
weather_train[:,10]=D
weather_train[:,11]=M


#n=0
#for i in range(20216100):
#    for j in range(139733):
#        n=n+1
#        print((n/2824856301300) * 100)
#        if (weather_train[:,0][j] == ds[:,6][i] and 
#            weather_train[:,9][j] == ds[:,2][i] and
#            weather_train[:,10][j] == ds[:,3][i] and
#            weather_train[:,11][j]== ds[:,4][i]):
#            
#            ds[:,11][i]=weather_train[:,2][j]
#            ds[:,12][i]=weather_train[:,3][j]
#            ds[:,13][i]=weather_train[:,4][j]
#            ds[:,14][i]=weather_train[:,5][j]
#            ds[:,15][i]=weather_train[:,6][j]
#            ds[:,16][i]=weather_train[:,7][j]
#            ds[:,17][i]=weather_train[:,8][j]       
