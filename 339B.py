# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 19:12:09 2021

@author: Aspire
"""

n = list(map(int,input().split()))

s = list(map(int,input().split()))

position = 1

count = 0

for i in range(0,n[1]):
    if s[i]>position:
        count = count + s[i] - position
        position = s[i]
    elif s[i]<position:
        count = count + n[0] - position + s[i]
        position = s[i]
    else:
        position = s[i]
print(count)