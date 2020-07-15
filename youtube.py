import numpy as np
from matplotlib import pyplot as plt

us_file_path = '/Users/peterpan/Downloads/DataAnalysis-master/day03/code/youtube_video_data/US_video_data_numbers.csv'
uk_file_path = '/Users/peterpan/Downloads/DataAnalysis-master/day03/code/youtube_video_data/GB_video_data_numbers.csv'

t_us = np.loadtxt ( us_file_path,delimiter=',',dtype='int')

#取评论的数据

t_us_comment = t_us[:,-1]
t_us_comment = t_us_comment[t_us_comment<5000]

#绘制直方图
print(t_us_comment.max() ,t_us_comment.min()  )

d = 250

bin_nums = ( t_us_comment.max()-t_us_comment.min() ) // d

#选择比五千小的数据

#绘图

plt.figure(figsize=(20,8),dpi = 80 )
plt.hist(t_us_comment,bin_nums)

plt.show()



#绘制 喜欢 和 评论的关系

import numpy as np
from matplotlib import pyplot as plt

us_file_path = '/Users/peterpan/Downloads/DataAnalysis-master/day03/code/youtube_video_data/US_video_data_numbers.csv'
uk_file_path = '/Users/peterpan/Downloads/DataAnalysis-master/day03/code/youtube_video_data/GB_video_data_numbers.csv'

t_uk = np.loadtxt ( uk_file_path,delimiter=',',dtype='int')

#选择喜欢数比 50W 小的数据

t_uk = t_uk[ t_uk[:,1] <= 500000 ]

t_uk_Comment = t_uk[ : , -1 ]
t_uk_like = t_uk[ :, 1 ]



#绘制散点图

plt.figure( figsize=(20,8), dpi=80 )
plt.scatter( t_uk_like ,t_uk_Comment )

plt.show( )