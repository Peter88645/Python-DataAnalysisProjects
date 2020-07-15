import pandas as pd
import numpy as np

file_path = '/Users/peterpan/Downloads/DataAnalysis-master/day05/code/starbucks_store_worldwide.csv'
df = pd.read_csv(file_path)

# print(df.head())
# print(df.info())

grouped = df.groupby(by='Country')
print( grouped )

#DataFrameGroupy
#可以进行 遍历
#调用聚合方法

# for i,j in grouped:
#     print('*'*100)
#     print(i)
#     print('-'*100)
#     print(j)


country_count = grouped['Brand'].count()
print(country_count['US'])
print(country_count['CN'])


#统计中国每个省份的店铺的国家的数量

china_data = df[df['Country']=='CN']
print( china_data.info())

grouped_CN = china_data.groupby(by ='State/Province').count()['Brand']
print(grouped_CN)

#数值按多个条件进行分组
#
# grouped = df['Brand'].groupby(by=[df['Country'],df['State/Province']]).count()
# print(grouped)
# print(type(grouped))



grouped2 = df[['Brand']].groupby(by=[df['Country'],df['State/Province']]).count()
print(type(grouped2))

#索引的方法和属性
print(grouped2.index)


