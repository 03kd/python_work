# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 18:45:18 2019

@author: keshav singh
"""

import numpy as np
from PIL import Image 

width =5
height=4

array= np.zeros([height,width,3],dtype=np.uint8)

img= Image.fromarray(array)
img.save("area_image.png")
#print('file is saved')

array1=np.zeros([100,200,3],dtype=np.uint8)
array1[:,:100]=[255,128,0] #orange
array1[:,100:]=[0,0,255]#blue

img=Image.fromarray(array1)
img.save("area_image2.png")