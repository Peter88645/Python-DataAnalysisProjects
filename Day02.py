# coding=utf-8

from matplotlib import pyplot as plt
from matplotlib import font_manager
import random

my_font = font_manager.FontProperties(fname='/Library/Fonts/Songti.ttc')

#y_3 = [random.randint(10,20) for i in range(31)]
#y_10 =[random.randint(14,20) for i in range(30)]

y_3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

x_3 = range(len(y_3))
x_10 = range(len(y_3)+10, len(y_10)+len(y_3)+10)
#设置图形大小

plt.figure(figsize=(20,8),dpi=80)


#使用scatter方法绘制 散点图， 和之前绘制 折线图的唯一区别

plt.scatter(x_3,y_3,label='三月份')
plt.scatter(x_10,y_10,label='十月份')

#调整 x轴的刻度
_x = list(x_3)+list(x_10)
_xticks_lable = ['三月{}日'.format(i) for i in x_3]
_xticks_lable += ['十月{}日'.format(i-40) for i in x_10]

plt.xticks(_x[::3],_xticks_lable[::3],fontproperties=my_font,rotation =45)


#添加描述信息
plt.xlabel('时间',fontproperties=my_font)
plt.ylabel('温度',fontproperties=my_font)
plt.title('三月和十月 温度随时间的变化统计表',fontproperties=my_font)

#添加图例
plt.legend(loc='upper left',prop=my_font)
#展示
plt.show()