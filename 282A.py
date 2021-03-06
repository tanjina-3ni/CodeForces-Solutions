# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 19:41:03 2021

@author: Aspire
"""

n = int(input())
c = 0
for i in range(0,n):
    x = input()
    if '+' in x:
        c = c+1
    else:
        c = c-1
print(c)