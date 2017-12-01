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

# train_gfp=np.array(_gfp[0:15])
# train_mcherry=np.array(_mcherry[0:15])
# test_gfp=np.array(_gfp[15])
# test_mcherry=np.array(_mcherry[15])
train_gfp=np.array(_gfp[1:16])
train_mcherry=np.array(_mcherry[1:16])
test_gfp=np.array(_gfp[0])
test_mcherry=np.array(_mcherry[0])

_x=tf.placeholder(tf.float32,[None,80])
_y=tf.placeholder(tf.float32,[None,80])

weight1=tf.Variable(tf.random_normal([80,160]))
bias1=tf.Variable(tf.zeros([1,160])+0.1)
output1=tf.nn.softmax(tf.matmul(_x,weight1)+bias1)

weight2=tf.Variable(tf.random_normal([160,160]))
bias2=tf.Variable(tf.zeros([1,160])+0.1)
output2=tf.nn.softmax(tf.matmul(output1,weight2)+bias2)

weight3=tf.Variable(tf.random_normal([160,80]))
bias3=tf.Variable(tf.zeros([1,80])+0.1)
output3=tf.nn.softmax(tf.matmul(output2,weight3)+bias3)

loss=tf.reduce_mean(tf.reduce_sum(tf.square(_y-output3),reduction_indices=[1]))

# optimizer=tf.train.GradientDescentOptimizer(0.1).minimize(loss)
optimizer=tf.train.AdamOptimizer(0.1,beta1=0.999).minimize(loss)

init=tf.initialize_all_variables()
sess=tf.Session()
sess.run(init)

for i in range(1000):
    _,loss_value=sess.run([optimizer,loss],feed_dict={_x:train_gfp,_y:train_mcherry})
    if(i%50==0):
        print(loss_value)

result_mcherry=sess.run(output3,feed_dict={_x:test_gfp.reshape((1,80))})

t=[i for i in range(80)]
plt.figure('gfp train set')
for i in range(15):
    plt.subplot(4,4,i+1)
    plt.plot(t,train_gfp[i])
plt.figure('mcherry train set')
for i in range(15):
    plt.subplot(4,4,i+1)
    plt.plot(t,train_mcherry[i])

plt.figure('gfp test set')
plt.plot(t,test_gfp)
plt.figure('mcherry test set')
plt.plot(t,test_mcherry)

plt.figure('mcherry test result')
plt.plot(t,result_mcherry[0])
plt.show()
plt.close()
