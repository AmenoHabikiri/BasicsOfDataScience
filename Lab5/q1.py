import numpy as np
import random
import matplotlib.pyplot as plt
X=[]
Y=[]
for i in range(0,1000000):
    X.append(random.randint(0,1))
    if (X[i]==0):
        k=random.random()
        if(k<=0.75):
            Y.append(0)
        else:
            Y.append(1)
    else:
        k=random.random()
        if(k<=0.65):
            Y.append(1)
        else:
            Y.append(0)
Xno_of_1=sum(X)
Xno_of_0=len(X)-sum(X)
Yno_of_1=sum(Y)
Yno_of_0=len(Y)-sum(Y)
print(Xno_of_0,Xno_of_1,Yno_of_0,Yno_of_1)
Y_X_0=(Yno_of_0/Xno_of_0)
Y_X_1=(Yno_of_1/Xno_of_1)
p_q=(Y_X_0-Y_X_1)/2
print(p_q)
