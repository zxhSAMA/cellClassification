__author__ = 'zhangxianghui'

import preProcess as pp
from matplotlib import pyplot as plt
import xlrd
import numpy as np
xls=xlrd.open_workbook('pulser.xlsx')
table=xls.sheets()[0]
# gfp=np.zeros((240,80))
# mcherry=np.zeros((240,80))
# index=np.array([1,74,157,261])
# for i in range(4):
#     for j in range(60):
#         gfp[i*60+j]=table.row_values(index[i]+j)[2:82]
#         mcherry[i*60+j] = table.row_values(index[i]+j)[82:162]
# x_train=np.zeros((240,160))
t=[i for i in range(80)]
gfp=np.array(table.row_values(1)[2:82],'float64')
mcherry=np.array(table.row_values(1)[82:162],'float64')
plt.figure(1)
plt.plot(t,gfp)
plt.plot(t,mcherry)
gfp=pp.mean_filt(gfp,[1,1,1,1,1])/3
mcherry=pp.mean_filt(mcherry,[1,1,1,1,1])/3
plt.figure(2)
plt.plot(t,gfp)
plt.plot(t,mcherry)

gfp=pp.L2_norm(gfp)
mcherry=pp.L2_norm(mcherry)
plt.figure(3)
plt.plot(t,gfp)
plt.plot(t,mcherry)
plt.show()