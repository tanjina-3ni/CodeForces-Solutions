# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 19:38:49 2021

@author: Aspire
"""

t = int(input())

for i in range(0,t):
    n = list(map(int,input().split()))
    n.sort()
    if n[0]==n[1]:
        print((n[0]+n[1])**2)
    elif n[0]<=(n[1]/2):
        print(n[1]**2)
    else:
        print((n[0]*2)**2)