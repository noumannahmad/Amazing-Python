# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:44:56 2021

@author: Nouman Ahmad
"""

from tkinter import *

from tkinter import messagebox
import random

root =Tk()

root.title("OTP Generator")
root.geometry("300x200")
    
root.config(bg="black")
def getotp():            
    messagebox.showinfo(title='OPT',message=f'Your OPT is:{random.randint(1000,9999)}')
    
    
label = Label(root,text="-----Click to Generate OPT -----",font=("arial",10,"bold"))
label.pack(fill=X,pady=5)
btn=Button(root,text="Generate",font=("arial",10,"bold"),command=getotp)  
btn.pack()

root.mainloop()  

        