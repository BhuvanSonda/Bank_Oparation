import numpy as np
from numpy import random
temp = np.array(random.randint(27,42,size=28))
re=temp.reshape(7,4)
days=np.array(['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'])
t_p=np.array(['morning','afternoon','evening'])

for i  in range(len(days)):
    print(days[i])
    for j in range(3):
        print("\t",t_p[j],'=',re[i][j])
    
    