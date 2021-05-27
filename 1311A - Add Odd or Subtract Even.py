# -*- coding: utf-8 -*-
"""
Created on Thu May 27 19:56:01 2021

@author: Aspire
"""

t = int(input())

for i in range(0,t):
    a,b = map(int,input().split())
    x = abs(a-b)
    if x==0:
        print(0)
    elif a<b:
        if x%2==0:
            print(2)
        else:
            print(1)
    else:
        if x%2==0:
            print(1)
        else:
            print(2)