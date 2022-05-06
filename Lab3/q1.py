import random
from matplotlib import pyplot as plt
import numpy as np
n=10000
array=[]
while (n<1000000):
    n+=10000
    h=0
    t=0
    for i in range(n):
        if (random.randint(0,1)==0):
            h+=1
        else :
            t+=1
    r=h/t
    array.append(r)
y1=[y for y in range(10000,1000000,10000)]
plt.plot(y1,array)
plt.show()