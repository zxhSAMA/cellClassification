__author__ = 'zhangxianghui'

import tensorflow as tf
import numpy as np
from numpy import linalg as la
from matplotlib import pyplot as plt
import xlrd

def getDataFromXlsx(file='',sheet=0,index=1,dose=1,scope=[2,82]):
    xls=xlrd.open_workbook(file)
    table=xls.sheets()[sheet]
    _data=np.array([])
    for i in range(table.nrows):
        if table.row_values(i)[index]==dose:
            _data=np.append(_data,table.row_values(i)[scope[0]:scope[1]])
    return _data.reshape((_data.size/(scope[1]-scope[0]),scope[1]-scope[0]))

def mean_filt(array,filter=[1,1,1]):
    l_filter=len(filter)
    l_array=len(array)
    Narray=np.append(array,[array[l_array-1] for k in range(l_filter-1)])
    res=np.zeros(l_array)
    for i in range(l_array):
        temp=[Narray[i+j] for j in range(l_filter)]
        res[i]=np.dot(temp,filter)
    return res

def L2_norm(x):  
    norm=la.norm(x)
    return x/norm

_gfp=getDataFromXlsx('pulser_with_response.xlsx',0,1,1,[2,82])
_mcherry=getDataFromXlsx('pulser_with_response.xlsx',0,1,1,[82,162])
for i in range(16):
    _gfp[i]=L2_norm(mean_filt(_gfp[i]))
    _mcherry[i]=L2_norm(mean_filt(_mcherry[i]))

_x=tf.placeholder(tf.float32,[None,80])
_y=tf.placeholder(tf.float32,[None,80])

weight=tf.Variable(tf.random_normal([80,80]))
bias=tf.Variable(tf.zeros([1,80])+0.1)
output=tf.nn.softmax(tf.matmul(_x,weight)+bias)
for i in range(1,10):
	output=tf.nn.softmax(tf.matmul(output,weight)+bias)

loss=tf.reduce_mean(tf.reduce_sum(tf.square(_y-output),reduction_indices=[1]))

optimizer=tf.train.AdamOptimizer(0.1,beta1=0.999).minimize(loss)

init=tf.initialize_all_variables()
sess=tf.Session()
sess.run(init)

for i in range(1000):
    _,loss_value=sess.run([optimizer,loss],feed_dict={_x:_gfp,_y:_mcherry})
    if(i%50==0):
        print(loss_value)

plat_gfp=np.zeros([1,80])+0.1
train_gfp=_gfp
plat_mcherry=sess.run(output,feed_dict={_x:plat_gfp})
train_mcherry=sess.run(output,feed_dict={_x:train_gfp})

t=[i for i in range(80)]
plt.figure('gfp train set')
for i in range(16):
    plt.subplot(4,4,i+1)
    plt.plot(t,_gfp[i])
plt.figure('mcherry train set')
for i in range(16):
    plt.subplot(4,4,i+1)
    plt.plot(t,_mcherry[i])
plt.figure('use plat gfp dataset train mcherry')
plt.plot(t,plat_mcherry[0])
plt.figure('use train gfp dataset train mcherry')
for i in range(16):
    plt.subplot(4,4,i+1)
    plt.plot(t,train_mcherry[i])
plt.show()
plt.close()
