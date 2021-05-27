# -*- coding: utf-8 -*-
"""
Created on Mon May 24 12:06:30 2021

@author: Aspire
"""

t = int(input())

for i in range(0,t):
    n,m = map(int,input().split())
    if n==1:
        print(0)
    elif n==2:
        print(m)
    else:
        print(2*m)
        