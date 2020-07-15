import numpy as np



#print(t1)
def fill_nbarray(t1):
    for i in range(t1.shape[1]): #遍历每一列
        temp_col = t1[:,i]  #当前的一列
        nan_num = np.count_nonzero(temp_col!=temp_col)
        if nan_num !=0:   #不为0 说明有nan
            temp_not_nan = temp_col[temp_col==temp_col]  #当前一列不为nan的array
            temp_col[np.isnan(temp_col)] = temp_not_nan.mean() #把当前不为nan的赋值为 不为nan的均值
    return t1


if __name__ == '__main__':
    t1 = np.arange(12).reshape((3, 4)).astype('float')
    t1[1, 2:] = np.nan
    print(t1)
    t1 = fill_nbarray(t1)
    print(t1)