# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 18:22:39 2019

@author: Abhay Kshirsagar
"""
import numpy as np
import sys
def restraints(board,i,j):
    for y in range(n):
        if board[i,y]==1:
            return False
    for x in range(n):
        if board[x,j]==1:
            return False
    for a,b in zip(range(i-1,-1,-1),range(j-1,-1,-1)):
        if board[a,b]==1:
            return False
    for a,b in zip(range(i-1,-1,-1),range(j+1,n,1)):
        if board[a,b]==1:
            return False
    return True

def val(board,ini,nsol):
    if ini==n:
        print("The number of possible solutions for board of size",n,"is",nsol)
        sys.exit()
    i=0
    board[i,ini]=1
    if fval(board,i,0):
        nsol+=1
        print("\n Solution no :",nsol)
        print(board)
        board = clear(board)
        val(board,ini+1,nsol)
    board[i,ini]=0
    clear(board)
    val(board,ini+1,nsol)

    
def fval(board,i,j):
    if i==n and counting(board):
        return True
    for y in range(i,n):
        for x in range(n):
            if restraints(board,y,x):
                board[y,x]=1
                if fval(board,y+1,x):
                    return True
                board[y,x]=0
    return False

def counting(board):
    t = 0
    for i in range(n):
        for j in range(n):
            if board[i,j]==1:
                t+=1
    if t==n:
        return True
    
def clear(board):
    for i in range(n):
        for j in range(n):
            if board[i,j]==1:
                board[i,j]=0
    return board

n=int(input("Enter the size of board eg. entering 4 will make a 4x4 board : "))
nsol = 0
#np.set_printoptions(threshold=np.nan)
board = np.zeros((n,n), dtype=int)
print(board)

if n>3:
    val(board,0,nsol)
else:
    print("size less than or equal to three is not allowed")