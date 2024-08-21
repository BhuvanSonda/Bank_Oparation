import matplotlib.pyplot as plt
import numpy as np
import sys

x=np.array([0,2,4,6])
y=np.array([0,8,3,5])

plt.plot(x,y,"o:")
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()




