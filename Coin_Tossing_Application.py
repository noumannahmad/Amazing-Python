# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:18:04 2021

@author: Nouman Ahmad
"""

import random

coin = ["Heads","Tails"]

toss =random.choice(coin)

selection = input("Please Choose Heads or Tails")

if selection == toss:
    print("You win! The coin landed on" + toss)
else:
 print("You loss! The coin landed on" + toss)
    
    