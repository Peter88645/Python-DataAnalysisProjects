import pandas as pd
import numpy as np
file_path = '/Users/peterpan/Downloads/DataAnalysis-master/dogNames2.csv'


# df = pd.read_csv(file_path)
#
# print(df)
#
# t = pd.DataFrame( np.arange(12).reshape((3,4)),index=list('abc'),columns=list('WXYZ') )
# print(t)
#
# d1 = {'name':['xiaoming','xiaogang'],'age':[20,32]}
#
#
# t1 = pd.DataFrame(d1)
# print(t1,type(t1))
#
# d2 = [ {'name':'xiaohong','age':32,'tel':100},{'name':'xiaohong','age':32},{'name':'xiaohong','tel':100}  ]
# t2 = pd.DataFrame(d2)
# print(t2)
#
#
#
# print(t.index)
# print(t.columns)


df = pd.read_csv(file_path)
# print( df.head() )
# print( df.info() )

# df = df.sort_values( by='Count_AnimalName',ascending=False)
# print(df.head(5))

#取前 20 行
#pandas 取行或者列的注意事项
'''
方括号 写数字 表示取行，对行进行操作 
写字符串 表示对列进行操作 
'''
#
# print( df[:20]['Row_Labels'] )
# print( type( df[ ['Row_Labels','Count_AnimalName'] ] ) )


t3 = pd.DataFrame( np.arange(12).reshape((3,4)),index=list('abc'),columns=list('WXYZ') )

# print( t3.loc['a','Z'] )
# print( t3.loc['a',: ] )
# print( t3.loc[ : ,'Y' ] )

# print(df.info())
# print(df.describe())
# print( df[ (80 < df['Count_AnimalName'])&(df['Count_AnimalName'] < 100) ] )
# print( df[ (df['Row_Labels'].str.len()<5)& (df['Count_AnimalName']<100 )  ] )

t3.iloc[1:, 0:2] = np.nan
print('*'*10)
print(t3)

print(t3.dropna(axis=0,how='any'))
print(t3.mean())
print(t3.fillna( t3.mean() ) )