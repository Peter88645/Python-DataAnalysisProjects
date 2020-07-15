import numpy as np

us_file_path = '/Users/peterpan/Downloads/DataAnalysis-master/day03/code/youtube_video_data/US_video_data_numbers.csv'
uk_file_path = '/Users/peterpan/Downloads/DataAnalysis-master/day03/code/youtube_video_data/GB_video_data_numbers.csv'

# 读取文件
t1 = np.loadtxt(us_file_path,delimiter=',',dtype='int',unpack=True)

# 把数据进行转置
t2 = np.loadtxt(us_file_path,delimiter=',',dtype='int')

print(t1)
print(t2)



#转置的方法
#方法1
# t3 = np.arange(24).reshape(4,6)
# print(t3)
# print(t3.transpose())
#
# #方法2
# print(t3.T)
#
# print('*'*100)
#
# #取行
# print(t2[2])
# print(t2[2: ])

print('*'*100)
# print(t2[[1,7,9]])

print(t2[1,:])
print(t2[2:,:])
#取第一列
print(t2[:,0])
print(t2[:,2:])

#取不连续的多列

# print(t2[:,[0,2]])

# a = t2[2,3]
# print(type(a))


#去多行多列， 取得是行和列交叉点的位置

# b = t2[2:5,1:4]
# print(b)


#取多个不相邻的点
# c = t2[[0,2],[0,1]]
# print(c)

t = np.arange(24).reshape(4,6)
np.where(t<3,0,10)
print(t)
print(np.where(t<3,0,10))

#裁剪
print(t.clip(10,20))

print(np.nan == np.nan)

#
t[:,0] = 0
print( np.count_nonzero(t) )

#统计 有多少个nan
#方法1

print(np.count_nonzero(np.isnan(t)))

print(t)
print( np.median(t,axis=1) )

print( np.ptp(t,axis=0))
print( t.std(axis=0) )