import cv2  as cv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn.linear_model as sk

df=pd.read_csv('data.csv')
# print(df)
# plt.scatter(df['Names'],df['A/C No:'],marker='*')

reg=sk.LinearRegression()
reg.fit(df[['A/C No:']],df['Balance :'])
plt.plot(df['A/C No:'],reg.predict(df[['Balance :']]),color='red')
plt.scatter(df['A/C No:'],df['Balance :'],marker='*')


plt.show()