import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import  font_manager

my_font = font_manager.FontProperties(fname='/Library/Fonts/Songti.ttc')
file_path = '/Users/peterpan/Downloads/DataAnalysis-master/day05/code/starbucks_store_worldwide.csv'
df = pd.read_csv(file_path)

#使用matplotlib呈现出店铺综述排名前十名的国家
#准备数据

grouped = df.groupby(by='Country').count()['Brand'].sort_values(ascending=False)[:10]
grouped2 = df.groupby(by='Country').count()
print(grouped)


_x  = grouped.index
_y = grouped.values

#画图
# plt.figure( figsize=(20,8),dpi=80 )
# plt.bar(_x,_y)
#
# plt.xticks(_x)
# plt.show()

df2 = df[df['Country']=='CN']
print(df2.info())


city_data = df2.groupby(by = 'City').count()['Brand'].sort_values(ascending=False)[:25]
_x  = city_data.index
_y = city_data.values

print(city_data)
# #画图
plt.figure( figsize=(20,8),dpi=80 )
#plt.bar(range(len(_x)),_y, width= 0.3,color = 'Orange')

plt.barh(range(len(_x)),_y, height= 0.3,color = 'Orange')

#plt.xticks(range(len(_x)),_x,fontproperties=my_font)
plt.yticks(range(len(_x)),_x,fontproperties=my_font)
plt.show()