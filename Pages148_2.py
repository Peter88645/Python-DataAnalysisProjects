import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager


file_path = '/Users/peterpan/Desktop/DataAnalysis-master/911.csv'

df = pd.read_csv(file_path)

# templist = df['title'].str.split(':').tolist()
# catlist =  [ i[0] for i in templist]
# df['cate'] = pd.DataFrame( np.array(catlist).reshape((df.shape[0],1)) )

#把时间字符串转化为 时间类型，设置为索引
df['timeStamp'] = pd.to_datetime(df['timeStamp'])


#设置添加列表示 分类
templist = df['title'].str.split(':').tolist()
cate_list = [ i[0] for i in templist ]
df['cate'] = pd.DataFrame( np.array(cate_list).reshape((df.shape[0],1)) )
'''
当我们把一列数据 复制到另一列数据里面的时候 ，一定要注意 索引必须 一致， 如果不一致的话 就会出现nan的问题
'''
df.set_index('timeStamp',inplace = True)

# print ( df['cate'] )

#分组

def graph(df):
    count_by_month = df.resample('M').count()['title']
    # 画图
    _x = count_by_month.index
    _y = count_by_month.values
    _x = [i.strftime('%Y-%m-%d') for i in _x]
    plt.plot(range(len(_x)), _y,label = groupe_name)
    plt.xticks(range(len(_x)), _x, rotation=45)
    plt.legend(loc='best')

#设置大小
plt.figure(figsize=(20, 8), dpi=80)

grouped = df.groupby(by='cate')
for groupe_name, groupe_data in grouped:
    #对不同的分类 都进行绘图
    graph(groupe_data)


plt.show()