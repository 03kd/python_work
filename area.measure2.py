# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 19:16:20 2019

@author: keshav singh
"""

from PIL import Image
im =Image.open("area_measure.png")
rgb_im =im.convert('RGB')
r,g,b=rgb_im.getpixel((1,1))
print(r,g,b)