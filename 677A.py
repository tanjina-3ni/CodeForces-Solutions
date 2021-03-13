# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 16:47:32 2021

@author: Aspire
"""

n = list(map(int,input().split()))

s = list(map(int,input().split()))

c = 0

for i in range(0,n[0]):
    if s[i] > n[1]:
        c = c + 2
    else:
        c = c + 1
print(c)