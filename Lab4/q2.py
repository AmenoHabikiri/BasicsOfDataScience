import random
from matplotlib import pyplot as plt
import numpy as np
N,p=list(map(float,input().split()))
N1=np.random.binomial(N,p,10000)
print(N1)
plt.hist(N1)
plt.show()
