#coding = utf-8

import numpy as np
from matplotlib import pyplot as plt

us_file_path = '/Users/peterpan/Downloads/DataAnalysis-master/day03/code/youtube_video_data/US_video_data_numbers.csv'
uk_file_path = '/Users/peterpan/Downloads/DataAnalysis-master/day03/code/youtube_video_data/GB_video_data_numbers.csv'

#加载国家数据
us_data = np.loadtxt( us_file_path, delimiter=',', dtype='int' )
uk_data = np.loadtxt( uk_file_path, delimiter=',', dtype='int' )

#添加国家信息
#构造全为零的数据
zero_data = np.zeros( (us_data.shape[0],1) ).astype('int')
ones_data = np.ones( (uk_data.shape[0],1) ).astype('int')

#添加全为0的数据
us_data = np.hstack( (us_data,zero_data) )

#添加全为1的数据
uk_data = np.hstack( (uk_data,ones_data) )

#拼接两组数据
final_data = np.vstack( (us_data,uk_data) )
print(final_data)

#创建一个对角线 为1 的正方形方阵
t = np.eye(4,7)
print( t )

print( np.argmax(t,axis= 1) )


#随机数
np.random.seed(0)
data_random = np.random.randint(10,20,(4,5))
#np.random.seed(0)
data_random2 = np.random.randint(10,20,(4,5))
print(data_random == data_random2)