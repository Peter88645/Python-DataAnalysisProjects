import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

file_path ='/Users/peterpan/Downloads/DataAnalysis-master/day05/code/IMDB-Movie-Data.csv'

df = pd.read_csv(file_path)
print(df.head(1))
rating_data = df['Rating'].values

print(type(rating_data))
print( rating_data )

max_rating = rating_data.max()
min_rating = rating_data.min()

#计算组数
print('*'*80)
print( max_rating-min_rating )

num_bin_list = [min_rating,1.6] + [0.5]*11
num_bin_list = np.cumsum(num_bin_list)
print( np.cumsum(num_bin_list) )

#设置图形大小
plt.figure(figsize=(20,8),dpi=80)

plt.hist( rating_data, num_bin_list )

#
# _x = [min_rating]
# print('rating is :', rating_data)
#
# i =  min_rating
# while i < max_rating:
#     i = i + (max_rating-min_rating)/7
#     _x.append(i)
#
#
# print(_x)

# 设置 x轴 的刻度

plt.xticks(num_bin_list)

#plt.grid()
#
plt.show()
