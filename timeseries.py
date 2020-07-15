import pandas as pd


t = pd.date_range(start ='20171230',end ='20181031',freq='10D')

t = pd.date_range(start ='20171230',periods=10,freq='D')

print(t)

#pandas 重采样