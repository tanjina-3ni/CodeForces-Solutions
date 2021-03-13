# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 16:08:03 2021

@author: Aspire
"""

n = int(input())

c = 0

for i in range(0,n):
    s = list(map(int,input().split()))
    
    if s[0]+2<=s[1]:
        c = c + 1
print(c)
    