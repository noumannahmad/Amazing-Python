# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 18:00:04 2021

@author: Nouman Ahmad
"""

from tkinter import *
from tkinter.ttk import *
from time import strftime

root =Tk()
root.title("World Clock")


def time():
    string=strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000,time)
    
    
lbl=Label(root,font=('calibri',40,'bold'),background='orange',foreground='white')

lbl.pack(anchor='center') 

time()
root.mainloop()   