# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 21:07:12 2021

@author: Aspire
"""

n = int(input())

c = 1
s = []
s.append(input())
for i in range(1,n):
    s.append(input())
    if s[i]!=s[i-1]:
        c = c + 1
print(c)