# -*- coding: utf-8 -*-
"""
Created on Sat May  8 22:27:58 2021

@author: Aspire
"""

t = int(input())

for i in range (0, t):
    x, y, n = map(int,input().split())
    k = int(n/x)
    while(1):
        if(x*k+y <= n):
            print(x*k+y)
            break
        else:
            k = k - 1