import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

file_path ='/Users/peterpan/Downloads/DataAnalysis-master/day05/code/books.csv'

df = pd.read_csv(file_path)
print(df.info())


data1 = df[pd.notnull(df['original_publication_year'])]

print(data1.info())

grouped = data1.groupby(by = 'original_publication_year').count()['title']


#不同年份书的平均评分情况
data2 = df[pd.notnull(df['original_publication_year'])]
grouped = data2[['average_rating']].groupby(by = data2['original_publication_year']).mean()

print(grouped)

_x = grouped.index
_y = grouped.values


#画图
plt.figure(figsize=(20,8),dpi=80)

plt.plot(range(len(_x)),_y)

plt.xticks(list(range(len(_x)))[::10],_x[::10].astype('int'),rotation=45)
plt.show()