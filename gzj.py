import numpy as np
x=np.array([[1,2,3],[4,5,6],[7,8,9]])
y=np.array([[1],[-1],[1]])
w=np.zeros([3,3])
b=np.zeros([3,1])
print(x[1])
print(x.shape[0])
for i in range(x.shape[0]):
    if np.dot(y[i],(np.dot(w[i].T,x[i])).T+b[i])<=0:
        w[i+1]=w[i]+np.dot(y.T,x[i])*0.01
        b[i+1]=b[i]+np.dot(y.T,x[i])*0.01
print(w)
print(b)
        
