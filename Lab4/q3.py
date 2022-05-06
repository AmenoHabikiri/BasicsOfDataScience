import random
from matplotlib import pyplot as plt
import numpy as np
p=float(input())
h=[]
for i in range(0,1000):
    k=0
    n=random.random()
    while (n>p):
        k+=1
        n=random.random()
    k+=1
    h.append(k)
print(h)
plt.hist(h,bins=max(h))
plt.show()



