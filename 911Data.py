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
catlist =  list(set([ i[0] for i in templist]) )

# print(catlist)

#构造全为0的数组
zeros_df = pd.DataFrame(np.zeros([df.shape[0],len(catlist)]),columns=catlist)

# print(zeros_df)

for cart in catlist:
    zeros_df[cart][df['title'].str.contains(cart)] = 1
    print(zeros_df)
    # break


# for i in range(df.shape[0]):
#     zeros_df.loc[i,templist[i][0]] = 1

sum_rect = zeros_df.sum(axis = 0)
print(sum_rect)

