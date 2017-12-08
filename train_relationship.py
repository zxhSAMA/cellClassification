__author__ = 'zhangxianghui'

from NeuralNetwork import NeuralNetwork
import numpy as np
import preProcess as pp

train_data=pp.unpickle('./train_set')
x=train_data['x'][0:60,0:80]
y=train_data['x'][0:60,80:160]

nn = NeuralNetwork([80,40,80], 'tanh')
nn.fit(x, y,learning_rate=0.1, epochs=10000)
# test_data=pp.unpickle('./test_set')
# print test_data
# test_num=test_data['number']
testx=np.ones(80)*100
# testy=test_data['y']
# predict=np.array([])
print(nn.predict(testx))
# for i in range(test_num):
#     print(np.append(nn.predict(testx[i]),[testy[i]]))
#     predict=np.append(predict,np.array(nn.predict(testx[i])))
# predict=predict.reshape((103,4))
# # print predict
# result=np.array([])
# for i in range(test_num):
#     row=predict[i]
#     max=np.where(row==np.max(row))
#     # print max
#     print(np.append(max[0][0]+1,[testy[i]]))
#     result=np.append(result,max[0][0]+1)
# rate=np.zeros(test_num)
# for i in range(test_num):
#     if result[i]==testy[i]:
#         rate[i]=1
# print sum(rate)/test_num