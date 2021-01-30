# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 15:58:42 2021

@author: Nouman ahmad
"""
import matplotlib.pyplot as plt

labels ='Slice_0','Slice_1','Slice_2','Slice_3'

Sizes =[15,30,45,10]

explode=(0,0.1,0,0)

fig1, ax1=plt.subplots()
ax1.pie(Sizes,explode=explode,labels=labels,
        autopct='%1.1f%%',shadow=True,startangle=90)

ax1.axis('equal')
plt.show()