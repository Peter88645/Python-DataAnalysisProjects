# coding = utf-8

from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager

#windows 和 linux 设置字体的方式

# font = {'family' : 'Microsoft YaHei',
#           'weight' : 'bold',
#         'size': 10}
#
# matplotlib.rc('font',**font)

#另一种方式 设置 字体
my_font = font_manager.FontProperties(fname='/Library/Fonts/Songti.ttc')

x = range(2,26,2)
y = [15,13,14,5,17,20,22,2,3,3,4,5]

print(len(x))



#设置图片大小
'''
 figure = (宽，高)
 dpi 图像清晰程度, 单位大小内 像素的个数 

'''
fig = plt.figure(figsize=(20,8),dpi = 80)

# 绘图
plt.plot(x,y)

#设置 x轴的刻度
'''
注意这里面 传的刻度 要与实际的 x 的相对应 比如可以传 range(25,50)看一下结果
'''
plt.xticks(range(25,50))
plt.yticks(range(min(y),max(y)+1))
#保存

'''
svg  矢量图格式，放大的时候 不会失真

'''
plt.savefig('./t1.png')
plt.show()



#============================#

x = range(0,120)
a = [random.randint(20,25) for i in range(120)]

#设置图片大小
plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,a)


#调整x轴的刻度
_x = list(x)
_xticks_lables = ['10H{}Minut'.format(i) for i in range(60)]
_xticks_lables +=['11H{}Minut'.format(i) for i in range(60)]

#取步长  数字和字符创 一一对应 数据的长度一样
#plt.xticks(_x[::3],_xticks_lables[::3],rotation=270,fontproperties=my_font)  # rotation=  旋转的度数

plt.xticks(_x[::3],_xticks_lables[::3],rotation=270)  # rotation=  旋转的度数

#解决不支持 中文的问题
'''
fc-list  查看支持的字体
fc-list :lang=zh  查看支持的中文
'''


#设置描述信息
plt.xlabel('time')
plt.ylabel('tempeture')
plt.title('the tempetrue statistics according to time')

plt.show()


#=================================================#
x = range(1,21)
y = [random.randint(1,3) for i in x]
y2 = [random.randint(4,8) for i in x]




#设置大小
plt.figure(figsize=(20,8),dpi=80)
plt.plot(x,y,label='David',color ='orange',linestyle ='--',linewidth=5)
plt.plot(x,y2,label='Peter',color='cyan',linestyle = ':')  # 画第二条 线

#设置 x y 轴的刻度
_xticks_lables = ['{}age'.format(i) for i in x]
plt.xticks(x,_xticks_lables)
plt.yticks(range(0,9))



#绘制网格
'''
alpha 设置透明度

'''
plt.grid(alpha=0.4)

#添加图例
plt.legend(loc='upper left')

plt.show()

