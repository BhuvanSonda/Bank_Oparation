import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import sys

data={"Date":[],'Product':[],'Quantity':[],'Price':[]}

class Update:
    def __init__(self):
        self.read=pd.read_csv("Store_data.csv") if pd.io.common.file_exists("Store_data.csv") else pd.DataFrame(columns=['Date','Product','Quanity','Price'])
    def update(date,product,quantity,price):
        data["Date"].append(date)
        data["Product"].append(product)
        data["Quantity"].append(quantity)
        data["Price"].append(price)
        df=pd.DataFrame(data)
        df.to_csv('Store_data.csv',mode='a+',index=False,header=not pd.io.common.file_exists('Store_data.csv'))

x=1
while(x!=0):
    print("enter 0 for exit else 1")
    x=int(input("enter your choice:"))
    if(x==0):
        sys.exit(0)
    p=input("Enter product name :")
    q=input("Enter quantity :")
    d=dt.date.today()
    pr=input("Enter price :")
    Update.update(d,p,q,pr)
