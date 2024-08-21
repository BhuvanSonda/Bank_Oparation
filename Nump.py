import numpy as np
from numpy import random as rm

a=np.array([1,5,3,4,6], dtype='f')
print(a)

# ar = numpy.array(['a', '2', '3'], dtype='i')#error
# print(ar)

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

arr=np.array(rm.randint(10,size=6))
print(arr)
x=np.where(arr)
print(x)

for i in arr:
    fact=1
    for j in range(1,i+1):
        fact*=j
    print(i,'=',fact)