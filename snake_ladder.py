# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 11:03:41 2019

@author: keshav singh
"""
from PIL import Image
import random
end = 100
def show_board():
    img =Image.open('s&l.jpg')
    img.show()
    
def check_ladder(points):
    if points==3:
        print("Ladder !!!")
        return 20
    
    elif points==6:
        print("Ladder !!!")
        return 14
    
    elif points==11:
        print("Ladder !!!")
        return 28
    
    elif points==15:
        print("Ladder !!!")
        return 34
    
    elif points==22:
        print("Ladder !!!")
        return 37
    
    elif points==17:
        print("Ladder !!!")
        return 74
    
    elif points==38:
        print("Ladder !!!")
        return 59
    
    elif points==49:
        print("Ladder !!!")
        return 67
    
    elif points==61:
        print("Ladder !!!")
        return 78
    
    elif points==88:
        print("Ladder !!!")
        return 91
    
    elif points==81:
        print("Ladder !!!")
        return 98
    else:
        return points
    
def check_snake(points):
    if points==26:
        print("Snake !!")
        return 10
    elif points ==39:
        print("Snake")
        return 5
    elif points ==51:
        print("Snake")
        return 6
    elif points ==56:
        print("Snake")
        return 1
    elif points ==60:
        print("Snake")
        return 23
    elif points ==75:
        print("Snake")
        return 28
    elif points ==93:
        print("Snake")
        return 25
    elif points ==99:
        print("Snake")
        return 63
    else:
        return points
    
def reached_end(points):
    if points==end:
        return True
    else:
        return False

def play():
    p1=input("Player 1 , enter your name : ")
    p2=input("Player 2 , enter your name : ")
    pp1=0
    pp2=0
    turn=0
    while(1):
        if turn%2 ==0:
            
            print(p1,'your turn')
            c=input("Press 1 to continue,0 for exit")
            if c==0:
                print(p1,' Scored ',pp1)
                print(p2,' Scored ',pp2)
                print("Thanks for playing")
                break
            dice=random.randint(1,6)
            print("Dice showed ",dice)
            
            pp1=pp1+dice
            pp1=check_ladder(pp1)
            pp1=check_snake(pp1)
            
            if pp1 >end:
                pp1=end
                
            print(p1,'Your score ',pp1)
            
            if reached_end(pp1):
                print(p1,"won")
                break
            
        else:
            print(p2,'your turn')
            c=input("Press 1 to continue,0 for exit")
            if c==0:
                print(p2,' Scored ',pp2)
                print(p1,' Scored ',pp1)
                print("Thanks for playing")
                break
            dice=random.randint(1,6)
            print("Dice showed ",dice)
            
            pp2=pp2+dice
            pp2=check_ladder(pp2)
            pp2=check_snake(pp2)
            
            if pp2 >end:
                pp2=end
                
            print(p2,'Your score ',pp2)
            
            if reached_end(pp2):
                print(p2,"won")
                break
        turn=turn+1



show_board()
play()