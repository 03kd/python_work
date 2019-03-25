# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 15:19:59 2019

@author: keshav singh
"""

for i in range(1,51):
     if(i%3==0 and i%5 ==0):
         print(str(i)+" = FizzBuzz")
     else:
         if(i%3==0):
          print(str(i)+" = Fizz")
         else:
            if(i%5==0):
             print(str(i)+" = Buzz")
            else:
             print(str(i))