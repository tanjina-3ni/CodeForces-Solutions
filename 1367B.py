# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 15:00:04 2021

@author: Aspire
"""

t = int(input())

for i in range(0,t):
    n = int(input())
    a = list(map(int,input().split()))
    c = 0
    d = 0
    for j in range(0,n):
        if j%2 != a[j]%2:
            if j%2==0:
                c = c + 1
            elif j%2!=0:
                d = d + 1
            
    if c==d:
        print(c)
    else:
        print('-1')