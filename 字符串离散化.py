import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

file_path ='/Users/peterpan/Downloads/DataAnalysis-master/day05/code/IMDB-Movie-Data.csv'

df = pd.read_csv(file_path)

print(df.head(1))
print(df['Genre'])


temp_list = df['Genre'].str.split(',').tolist()
genre_list = list(set(  [i for j in temp_list for i in j ] ) )

#print('*'*100)
#print(temp_list)
# df[genre_list] =np.zeros(1000)

zeros_df = pd.DataFrame(np.zeros( (df.shape[0],len(genre_list)) ),columns=genre_list)

#print( zeros_df )


#给每个电影出现分类的位置 复制

for i in range(df.shape[0]):
    zeros_df.loc[i,temp_list[i]] = 1

print(zeros_df)

#统计每个分类的电影的和

genre_count = zeros_df.sum(axis = 0)
print(genre_count)

#排序
print(genre_count.sort_values())

genre_count=genre_count.sort_values()

_x = genre_count.index
_y = genre_count.values

print(_y)
print(_x)

#画图
plt.figure(figsize=(20,8),dpi=80)
plt.bar( range(len(_x)), _y ,width=0.7,color ='orange')

#设置x轴 参数
plt.xticks(range(len(_x)),_x)

plt.show()

