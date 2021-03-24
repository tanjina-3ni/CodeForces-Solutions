# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 14:11:44 2021

@author: Aspire
"""

t = int(input())

for i in range(0,t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    
    mina = min(a)
    minb = min(b)
    
    j = 0
    c = 0
    while(j<n):
        if a[j]>mina or b[j]>minb:
            if a[j]>mina and b[j]>minb:
                x = a[j] - mina
                y = b[j] - minb
                c = c + max(x,y)
            elif a[j]>mina:
                x = a[j] - mina
                c = c + x
            elif b[j]>minb:
                y = b[j] - minb
                c = c + y
        j = j + 1
    print(c)
        