__author__ = 'zhangxianghui'

import xlrd
import numpy as np
import matplotlib.pyplot as plt


def mean_filt(array,filter=[1,1,1]):
    import numpy as np
    l_filter=len(filter)
    l_array=len(array)
    Narray=np.append(array,[array[l_array-1] for k in range(l_filter-1)])
    res=np.zeros(l_array)
    for i in range(l_array):
        temp=[Narray[i+j] for j in range(l_filter)]
        res[i]=np.dot(temp,filter)
    return res

def L2_norm(x):
    from numpy import linalg as la
    norm=la.norm(x)
    return x/norm

def pickle(file,data,opt='wb'):
    import cPickle
    with open(file,opt) as fw:
        cPickle.dump(data,fw)
    return

def unpickle(file,opt='rb'):
    import cPickle
    with open(file,opt) as fr:
        data=cPickle.load(fr)
    return data

data=xlrd.open_workbook('pulser.xlsx')
# print data
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols
print nrows
print ncols
# for i in range(344):
#     print table.row_values(i)
#     print "\n"

trow=table.row_values(2)
print trow

y=np.array([trow[i] for i in range(2,162)])

yy=mean_filt(y,[1,1,1,1,1,1,1])

# norm=la.norm(yy)
# yyy=yy/norm
yyy=L2_norm(yy)
# pickle('./data',yyy)
# print unpickle('./data')

x=np.array([i for i in range(0,160)])
plt.figure(1)
plt.plot(x,y)

plt.figure(2)
plt.plot(x,yy)

plt.figure(3)
plt.plot(x,yyy)
plt.show()
plt.close()