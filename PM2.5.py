import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

pd.set_option('display.max_columns', None)   #显示完整的列

file_path = '/Users/peterpan/Desktop/DataAnalysis-master/day06/code/PM2.5/BeijingPM20100101_20151231.csv'
df = pd.read_csv(file_path)

# print( df.head() )
# print( df.info() )


#把分开的时间 字符串，通过PeriodIndex 的方法转化为 pandas的时间类型

period = pd.PeriodIndex(year = df['year'],month = df['month'],day = df['day'],hour =df['hour'],freq='H')
print(period)
# print( type(period) )

df['datatime'] = period
print(df.head(10))

#把 datetime设置为 索引
df.set_index(period, inplace = True)
print(df.head(10))

#进行降采样
df = df.resample('7D').mean()


#处理缺失数据

#把缺失值直接删掉
# PM_US_data = df( df['PM_US Post']==df['PM_US Post'] )
print(['*']*100)
# print(df['PM_US Post'].dropna())


# print(df['PM_Dongsi'].tail(20))

# data = df['PM_US Post'].dropna()
# data_CN = df['PM_Dongsi'].dropna()
data = df['PM_US Post']
data_CN = df['PM_Dongsi']


#画图
_x = data.index
_y = data.values

_x_cn = data_CN.index
_y_cn = data_CN.values

plt.figure(figsize=(20,8),dpi=80 )
plt.plot(range(len(_x)),_y , label ='US')
plt.plot( range(len(_x_cn)),_y_cn,label = 'CN')

plt.xticks(list(range(len(_x)) )[::10],_x[::10],rotation = 45 )
plt.legend(loc = 'best')
plt.show()