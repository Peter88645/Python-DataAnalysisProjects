from matplotlib import pyplot as plt
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname ='/Library/Fonts/Songti.ttc')

#数据
a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]

#设置大小
plt.figure(figsize=(20,8),dpi=80)


#绘制多次 画法1

# plt.bar(range(len(a)),b_14,width=barwidth)
# plt.bar(range(len(a)+3,2*len(a)+3),b_15,width=barwidth)
# plt.bar(range(2*len(a)+6,3*len(a)+6),b_16,width=barwidth)

#绘制多次 画法2
barwidth = 0.2
x_14 =list(range(len(a)))
x_15 =[ i+barwidth for i in x_14 ]
x_16 =[ i+barwidth for i in x_15 ]

plt.bar(x_14,b_14,width=barwidth,label='14号票房')
plt.bar(x_15,b_15,width=barwidth,label='15号票房')
plt.bar(x_16,b_16,width=barwidth,label='16号票房')

#把名字对应到 x 轴

#对应画法1
#_xticks_lable = a+['','','']+a+['','','']+a
#plt.xticks(range(len(a)*3+6),_xticks_lable,fontproperties= my_font,rotation=90)

#对应画法2
# _x = x_14+x_15+x_16
# _xticks_lable2 = a*3

plt.xticks(x_15,a,fontproperties= my_font,rotation=0)

#添加图例
plt.legend(loc='upper left',prop=my_font)

#添加图标信息
plt.xlabel('电影的名字',fontproperties=my_font)
plt.ylabel('票房',fontproperties=my_font)
plt.title('14日15日16日 三次票房的对比',fontproperties=my_font)


plt.show()
