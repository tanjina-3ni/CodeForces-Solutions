# -*- coding: utf-8 -*-
"""
Created on Fri May  7 22:16:52 2021

@author: Aspire
"""

def isPrime(x):
    c = 0
    for i in range(2,int(x/2)+1):
        if x%i == 0:
            c = 1
            break;
    if c == 1:
        return 0
    else:
        return 1

n = int(input())

for x in range(int(n**(0.5)),n):
    y = n-x
    #print(x,y)
    a = isPrime(x)
    b = isPrime(y)
    #print(a)
    if a==0 and b==0:
        print(x,y)
        break
    

