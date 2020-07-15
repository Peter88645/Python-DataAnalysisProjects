import pandas as pd
import numpy as np

file_path ='/Users/peterpan/Downloads/DataAnalysis-master/day05/code/IMDB-Movie-Data.csv'

df_movie = pd.read_csv(file_path)

print(df_movie.head(1))

print(df_movie.info())

print(df_movie.describe())


print('*'*100)
#获取电影的平均评分
print(df_movie['Rating'].mean())

#导演的人数
print( len(set( df_movie['Director'].tolist())))
print(df_movie['Director'].nunique())

#获取演员的人数

temp_actor_list = df_movie['Actors'].str.split(',').tolist()

print(df_movie['Actors'])

actors_list = [i for j in temp_actor_list for i in j ]
print(len(set(actors_list)))


