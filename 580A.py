# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 21:44:15 2021

@author: Aspire
"""

n = int(input())
s = list(map(int, input().split()))
m = 0
c = 0
for i in range(1, n):
    if s[i-1]<=s[i]:
        c = c + 1
        #print(c)
    else:
        if c > m:
            m = c
        c = 0
if c>m:
    m = c        
print(m+1)