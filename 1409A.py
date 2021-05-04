# -*- coding: utf-8 -*-
"""
Created on Tue May  4 13:25:43 2021

@author: Aspire
"""

t = int(input())

for i in range(0,t):
    a,b = map(int,input().split())
    
    diff = abs(a-b)
    
    if diff==0:
        print(0)
    elif diff<=10:
        print(1)
    else:
        x = int(diff/10)
        if diff%10==0:
            print(x)
        else:
            print(x+1)