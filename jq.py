import numpy as np
x=np.array([[1,1,1,0,0,0],
         [0,0,0,0,1,1],
         [0,0,0,1,0,1],
         [1,0,0,0,1,1],
         [0,0,0,1,0,1],
         [1,1,1,0,1,0],
         [0,1,0,1,0,0],
         [1,0,0,0,1,1],
         [0,1,0,0,0,1]])
print(x.shape[0])
y=np.array([[0,0,0,1,1,1]])
print(y.shape[0])
dim=x.shape[0]
w=np.random.random((dim,1))
cost=1/(1+np.exp(np.dot(w.T,x)))-y
print(cost)
for i in range(1000):
    w=w+0.001*np.dot(1/(1+np.exp(np.dot(w.T,x))),(1/(1+np.exp(np.dot(w.T,x)))).T)
print(cost)
print(w)
d=np.array([[1],[0],[0],[0],[1],[0],[0],[0],[1]])
cst=1/(1+np.exp(np.dot(w.T,d)))-1
ost=cost=1/(1+np.exp(np.dot(w.T,d)))-0
print(cst)
print(ost)
