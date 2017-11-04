__author__ = 'zhangxianghui'

if __name__=='__main__':
    import preProcess as pp
    import xlrd
    import numpy as np
    xls=xlrd.open_workbook('pulser.xlsx')
    table=xls.sheets()[0]
    gfp=np.zeros((240,80))
    mcherry=np.zeros((240,80))
    index=np.array([1,74,157,261])
    for i in range(4):
        for j in range(60):
            gfp[i*60+j]=table.row_values(index[i]+j)[2:82]
            mcherry[i*60+j] = table.row_values(index[i]+j)[82:162]
    x_train=np.zeros((240,160))
    for i in range(240):
        gfp[i]=pp.L2_norm(pp.mean_filt(gfp[i], [1, 1, 1, 1, 1]))
        mcherry[i]=pp.L2_norm(pp.mean_filt(mcherry[i], [1, 1, 1, 1, 1]))
        x_train[i]=np.append(gfp[i],mcherry[i])
    y_train=np.concatenate((np.ones(60),2*np.ones(60),3*np.ones(60),4*np.ones(60)))
    train_set={'name':'train_set','number':240,'x':x_train,'y':y_train}
    # pp.pickle('./train_set',train_set)
    print pp.unpickle('./train_set')