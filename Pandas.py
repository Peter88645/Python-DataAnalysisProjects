import pandas as pd
#print( pd.Series([1,2,3,4,5],index=list('abcde') ) )


temp_dict = {'name':'xiaohong','age':23 }
t3 = pd.Series(temp_dict)
# print(t3['age'])
# print(t3[1])
# print(t3[:2])
print(t3[['age','name']])
print(t3.index)
print(t3.values)


