# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:00:26 2021

@author: Nouman Ahmad
"""

import tkinter as tk
import pyautogui

root=tk.Tk()
root.title("Screenshot")
root.geometry("350x350")


def capturescreenshot():
    screenshort = pyautogui.screenshot()
    screenshort.save('screenshort.png')
    
btn = tk.Button(root,text="Capture Screen",command=capturescreenshot)

btn.pack()
root.mainloop()    