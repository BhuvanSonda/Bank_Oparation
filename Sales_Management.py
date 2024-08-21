import numpy as np
from numpy import random
import pandas as pd
import matplotlib.pyplot as plt
import sys 

months=["Jan","Feb","Mar",'Apr','May','Jun','Jul','Agu','Sep',"Oct",'Nov','Dec']
values=np.array(random.randint(2000,3500,size=12)) 

data={'Months':months,
      'Sales':values}

df = pd.DataFrame(data)

df.to_csv("salessheet.csv","w",index=False)

read=pd.read_csv("salessheet.csv")

x_axis = months
y_axis = values
plt.plot(x_axis,y_axis,marker='*',ms=10,c='r',mfc='y',mec='g')
plt.grid(ls='dotted',color="y")

f1={'family':'serif','color':'b',"size":20}
f2={'family':'serif','color':'brown',"size":15}

plt.title('"Monthly Sales Data"',fontdict=f1)
plt.xlabel("Months",fontdict=f2)
plt.ylabel("Sales",fontdict=f2)

plt.show()

# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()
