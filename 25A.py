# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 15:38:50 2021

@author: Aspire
"""

n = input()

s = list(map(int, input().split()))
c = 0

for i in range(0,3):
    c = c + s[i] % 2

for i in range(0,len(s)):
    if c<2 and s[i] % 2 == 1:
        print(i + 1)
        break
    elif c>=2 and s[i] % 2 == 0:
        print(i + 1)
        break
    
