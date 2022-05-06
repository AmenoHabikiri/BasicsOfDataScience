import random
from matplotlib import pyplot as plt
import numpy as np
lii=[]
for k in range(0,1000):
    n=50
    li=[]
    li2=[0 for x in range(0,365)]
    for i in range(0,n):
        r=random.randint(0,365)
        li.append(r)
    for i in range(0,365):
        for j in range(0,n):
            if (i==li[j]):
                li2[i]+=1
    li2.sort(reverse=True)
    lii.append(li2[0])

X=[x for x in range(0,1000)]
plt.plot(X,lii)
prob=0
for i in range(0,len(lii)):
    if (lii[i]>=2):
        prob+=1
print(prob/len(lii))


