import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager


file_path = '/Users/peterpan/Desktop/DataAnalysis-master/911.csv'

df = pd.read_csv(file_path)
print(df.head(10))
print(df.info())

#获取分类情况

# print(df['title'].str.split(':'))
templist = df['title'].str.split(':').tolist()
catlist =  [ i[0] for i in templist]

df['cate'] = pd.DataFrame( np.array(catlist).reshape((df.shape[0],1)) )
print('*'*100)
print(df['cate'])

# df['cart']

# print(df.head(5))
#
# grouped = df.groupby(by='cate').count()['title']
# print(grouped)