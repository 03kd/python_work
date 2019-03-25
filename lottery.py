# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 17:30:25 2019

@author: keshav singh
"""

import random
import matplotlib.pyplot as plt

account = 0
x=[]
y=[]
for i in range(365):
    x.append(i+1)
    bet = random.randint(1,10)
    
    lucky_draw = random.randint(1,10)
    
    #print(lucky_draw)
    
    if bet == lucky_draw:
        account = account+800
    
    else:
        account=account -100
    y.append(account)
    
print("Your balance is ",account)

plt.plot(x,y)
plt.show()