# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 19:10:36 2021

@author: Aspire
"""

t = int(input())

for i in range(0,t):
    b = input()
    if len(b)==2:
        print(b)
    else:
        i = 2
        a = b[0]
        while(i<len(b)):
            if b[i-1]==b[i]:
                a = a + b[i]
                i = i + 1
            i = i + 1
        a = a + b[len(b)-1]
        print(a)