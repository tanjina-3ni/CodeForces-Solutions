# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 23:03:05 2021

@author: Aspire
"""

s = input().split()

k = int(s[0])
n = int(s[1])
w = int(s[2])

cost = int((w*(w+1)*k/2)-n)

if cost<=0:
    print(0)
else:
    print(cost)