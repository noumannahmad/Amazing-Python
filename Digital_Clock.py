# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:31:23 2021

@author: Nouman Ahmad
"""

from tkinter import *
import time

def times():
    
    current_time = time.strftime("%I:%M:%S:%p")
    clock_lbl = Label(root,font="berlin 80",bg="white",fg="black",text=current_time)
    clock_lbl.after(200,time)
    clock_lbl.grid(row=0,column=1)
    
root=Tk()
root.title("Digital Clock")
root.resizable(False,False)
times()
root.mainloop()