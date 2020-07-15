import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

file_path ='/Users/peterpan/Downloads/DataAnalysis-master/day05/code/IMDB-Movie-Data.csv'

df = pd.read_csv(file_path)
print(df.head(1))
print(df.info())

#rating ,runtime 分布情况

#选择图形, 直方图
#runtime_data = df['Runtime (Minutes)'].values

runtime_data = df['Rating'].values

print(type(runtime_data))
print( runtime_data )

max_runtime = runtime_data.max()
min_runtime = runtime_data.min()

#计算组数
print('*'*80)
print( max_runtime-min_runtime )
bin_nums = (max_runtime-min_runtime)//0.5
print(bin_nums)
#设置图形大小
plt.figure(figsize=(20,8),dpi=80)

plt.hist( runtime_data, int(bin_nums) )
_x = [min_runtime]
i = min_runtime
print('max_runtime is :', max_runtime)

while i < max_runtime:
    i = i + (max_runtime-min_runtime)/7
    _x.append(i)


print(_x)
# plt.xticks(range(min_runtime,max_runtime+0.5,0.5))
plt.xticks(_x)

plt.grid()
#
plt.show()