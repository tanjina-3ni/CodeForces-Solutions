# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 16:42:58 2021

@author: Aspire
"""

n = input().split()

s = input().split()

c = 0

for i in range(0, len(s)):
    if int(s[i])>= int(s[int(n[1])-1]) and s[i]>'0':
        c = c + 1
print(c)


