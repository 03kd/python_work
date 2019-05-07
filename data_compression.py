# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 10:53:29 2019

@author: keshav singh
"""

import numpy as np

from PIL import Image

im=Image.open('lena.jpg')

pixelmap=im.load()

img = Image.new(im.mode,im.size)
pixelNew =img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        if (pixelmap[i,j]>=0 and pixelmap[i,j]<=31):
            pixelNew[i,j]=0
            
        elif (pixelmap[i,j]>=32 and pixelmap[i,j]<=63):
            pixelNew[i,j]=1
        
        elif (pixelmap[i,j]>=64 and pixelmap[i,j]<=95):
            pixelNew[i,j]=2
            
        elif (pixelmap[i,j]>=96 and pixelmap[i,j]<=127):
            pixelNew[i,j]=3
            
        elif (pixelmap[i,j]>=128 and pixelmap[i,j]<=159):
            pixelNew[i,j]=4
        
        elif (pixelmap[i,j]>=160 and pixelmap[i,j]<=191):
            pixelNew[i,j]=5
        
        elif (pixelmap[i,j]>=192 and pixelmap[i,j]<=223):
            pixelNew[i,j]=6
        
        elif (pixelmap[i,j]>=224 and pixelmap[i,j]<=255):
            pixelNew[i,j]=7
                    
img.save('lena_2.jpg')
         
j =np.asanyarray(Image.open('lena_2.jpg'))
         
         
         
         
         
         
         
         
         
         
         
        
        