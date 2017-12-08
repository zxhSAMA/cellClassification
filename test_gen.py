__author__ = 'zhangxianghui'

if __name__=='__main__':
    import preProcess as pp
    import xlrd
    import numpy as np
    xls=xlrd.open_workbook('pulser.xlsx')
    table=xls.sheets()[0]
    gfp=np.zeros((103,80))
    mcherry=np.zeros((103,80))
    num=np.array([13,23,44,23])
    index=0
    for i in range(4):
        for j in range(num[i]):
            gfp[index]=table.row_values((i+1)*60+j+1)[2:82]
            mcherry[index]=table.row_values((i+1)*60+j+1)[82:162]
            index=index+1
    x_test=np.zeros((103,160))
    for i in range(103):
        gfp[i]=pp.mean_filt(gfp[i], [1, 1, 1, 1, 1])/5
        mcherry[i]=pp.mean_filt(mcherry[i], [1, 1, 1, 1, 1])/5
        x_test[i]=np.append(gfp[i],mcherry[i])
    y_test=np.concatenate((np.ones(13),2*np.ones(23),3*np.ones(44),4*np.ones(23)))
    test_set={'name':'test_set','number':103,'x':x_test,'y':y_test}
    # pp.pickle('./test_set',test_set)
    print pp.unpickle('./test_set')