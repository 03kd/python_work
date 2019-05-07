# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 16:12:42 2019

@author: keshav singh
"""

import scipy.misc
from PIL import Image
import numpy as np
import random

img=scipy.misc.imread("punjab.png")
count_pun=0
count_in=0
count=0
while(count<=10000):
    x=random.randint(0,2735)
    y=random.randint(0,2480)
    z=0
    if(img[x][y][z]==196):
        count_in=count_in+1
        count+=1
        
    else:
        if(img[x][y][z]==242):
            count_pun = count_pun+1
            count =count+1
print(count_pun)
print(count_in)          
area_pun=(count_pun/count_in)*3287263
print(area_pun)