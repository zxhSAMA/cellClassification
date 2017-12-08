__author__ = 'zhangxianghui'

from NeuralNetwork import NeuralNetwork
import numpy as np
import preProcess as pp
from sklearn.preprocessing import LabelBinarizer

train_data=pp.unpickle('./train_set')
x=train_data['x']
y=train_data['y']
labels_train = LabelBinarizer().fit_transform(y)
nn = NeuralNetwork([160,40,4], 'tanh')
nn.fit(x, labels_train,learning_rate=0.1, epochs=10000)
test_data=pp.unpickle('./test_set')
# print test_data
test_num=test_data['number']
testx=test_data['x']
testy=test_data['y']
predict=np.array([])
for i in range(test_num):
    print(np.append(nn.predict(testx[i]),[testy[i]]))
    predict=np.append(predict,np.array(nn.predict(testx[i])))
predict=predict.reshape((103,4))
# print predict
result=np.array([])
for i in range(test_num):
    row=predict[i]
    max=np.where(row==np.max(row))
    # print max
    print(np.append(max[0][0]+1,[testy[i]]))
    result=np.append(result,max[0][0]+1)
rate=np.zeros(test_num)
for i in range(test_num):
    if result[i]==testy[i]:
        rate[i]=1
print sum(rate)/test_num



# from matplotlib import pyplot as plt
# t=[i for i in range(80)]
# for i in range(4):
#     plt.figure(i+1)
#     k=0
#     for j in range(60*i,60*(i+1)):
#         plt.subplot(6, 10, 1+k)
#         plt.plot(t,x[j][0:80])
#         plt.plot(t,x[j][80:160])
#         plt.axis('off')
#         k=k+1
# plt.show()
