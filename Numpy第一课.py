import numpy as np
import random

#使用numpy生成数组

t1 = np.array([1,2,3,])
print(t1)
print(type(t1))

t2 = np.array(range(10))
print(t2)
print(type(t2))

t3 = np.arange(3,10,2)
print(t3)
print(type(t3))


print(t3.dtype)


#numpy 中的数据类型

t4 = np.array(range(1,4),dtype='float32')
print(t4)
print(t4.dtype)

#numpy 中的布尔类型
t5 = np.array([1,1,0,1,0],dtype=bool)
print(t5)
print(t5.dtype)


#调整数据类型
t6 = t5.astype('int8')
print(t6)
print(t6.dtype)

#numpy 中的小数

t7 = np.array( [random.random() for i in range(10)] )

print(t7)
print(t7.dtype)

t8 = np.round(t7,3)
print(t8)



#多维数组

t9 = np.arange(24).reshape((2,3,4))

print(t9)

print( t9.reshape((4,6)) )
print(t9.reshape(24,))
print(t9.reshape(24,1))
print(t9.reshape(1,24))

print(t9.reshape((t9.shape[0]*t9.shape[1]*t9.shape[2],)) )
print(t9.flatten())



#运算

t5 = np.arange(24).reshape((4,6))
print(t5)
print(t5+2)



#形状不完全一样的时候 也是可以计算的
#广播机制
#但是如果行 和列 都不相同的话 那么是不能一起计算的

t51=np.arange(6).reshape((6,))
print(t5)
print(t5-t51)

t52=np.arange(4).reshape((4,1))
print(t5-t52)


t = np.arange(18).reshape((3,3,2))
tt = np.arange(6).reshape((3,2))
print(t-tt)