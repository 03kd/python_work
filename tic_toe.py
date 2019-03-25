# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 16:55:07 2019

@author: keshav singh
"""

import numpy

board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])

p1='X'
p2='O'

def check_rows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count=count+1
        if count==3:
            print(symbol,'won !!!')
            return True
    return False
    
def check_columns(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if board[r][c]==symbol:
                count=count+1
        if count==3:
            print(symbol,'won !!!')
            return True
    return False
def check_diagonal(symbol):
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[2][0]==symbol:
        print(symbol,' Won ')
        return True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[2][2]==symbol:
        print(symbol,' Won ')
        return True
    return False

def won(symbol):
    return check_rows(symbol) or check_columns(symbol) or check_diagonal(symbol) 

def place(symbol):
    print(numpy.matrix(board))
    while(1):
        row=int(input('Enter row -1,2 or3'))
        col=int(input('enter col-1,2 or 3'))
        if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-':
            break
        else:
            print("Invalid input.Please enter correct input")
    board[row-1][col-1]=symbol
    
def play():
    for turn in range(9):
        if turn%2==0:
            print('X turn')
            place(p1)
            if won(p1):
                break
        else:
            print('O turn')
            place(p2)
            if won(p2):
                break
        if not(won(p1)) and(won(p2)):
            print("Draw")
            
play()
        
        
        
        
        
        
        
        
        
        
        
        
        
        