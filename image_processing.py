# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 11:51:19 2019

@author: keshav singh
"""
'''
#flipping of image
from PIL import Image
#importing the image from file location
img = Image.open('mirror.png')
#image in matrix format so transposing give real image
transposed =img.transpose(Image.FLIP_LEFT_RIGHT)
#new real image is formed and saved
transposed.save('mirror_reverse.png')

print("Flipping is done ")
'''

#image Enhancement using CLAHE technique
import cv2

img=cv2.imread('bullets.png')
#Prepartion for CLAHE
clahe=cv2.createCLAHE()

#Convert into grey scale image
gray_img =cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)

#Applying Enhancement 
enh_img = clahe.apply(gray_img)

#save to file
cv2.imwrite('enhanced.png',enh_img)

print("Done Enhancing")


















