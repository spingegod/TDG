import numpy as np
import pandas as pd

train = pd.read_csv('train.csv')
A = pd.to_datetime(train['timestamp'],format='%Y-%m-%d %H:%M:%S')
train['timestamps'] = A
