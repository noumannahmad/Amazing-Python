# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 15:29:33 2021

@author: Nouman Ahmad
"""

from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo
import random

root=tk.Tk()

root.title("Random Number Geneator")

def dice():
    random_number=random.randint(1, 6)
    randomno.config(text='Number is: {random_number}')
    if random_number == 6:
        showinfo('Congratulations','YOU WON')



randomno=ttk.Label(root,text="")
randomno.pack(pady=10)

play=ttk.Button(root,text="Play",command=dice)
play.pack(padx=50)
root.mainloop()        
        
        