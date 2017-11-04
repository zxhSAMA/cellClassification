__author__ = 'zhangxianghui'

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
