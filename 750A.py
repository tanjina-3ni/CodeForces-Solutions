# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 22:25:19 2021

@author: Aspire
"""

n,k = map(int,input().split())

k = 240 - k
i = 1

while(i<=n):
    k = k - 5*i
    if k<0:
        break
    i = i + 1

print(i-1)
#print(n,k)