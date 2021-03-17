# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 18:52:17 2021

@author: Nouman Ahmad
"""

import winsound

frequency =2500
duration=1000

winsound.Beep(frequency,duration)

def sos():
    for i in range(0,3):
        winsound.Beep(2000, 100)
        for i in range(0,3):
            winsound.Beep(2000, 400)
            for i in range(0,3):
                winsound.Beep(2000, 100)
                 
sos()                 
            