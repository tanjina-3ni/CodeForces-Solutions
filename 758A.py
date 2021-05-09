# -*- coding: utf-8 -*-
"""
Created on Sun May  9 22:05:23 2021

@author: Aspire
"""

n = int(input())

l = list(map(int,input().split()))

m = max(l)
s = 0
for i in range(0,len(l)):
    s = s + (m - l[i])

print(s)