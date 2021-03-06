# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 22:16:31 2021

@author: Aspire
"""

n = int(input())
c = 0
s = input()
for i in range(0,len(s)):
    #print(i,s[i])
    if s[i-1] == s[i] and i>=1:
        c = c + 1
print(c)
    