# -*- coding: utf-8 -*-
"""
Created on Sat May 29 15:19:27 2021

@author: Aspire
"""

a = list(map(int,input().split()))
b = list(map(int,input()))

i = 0
s = 0
while i<4:
    c = b.count(i+1)
    s = s + (a[i] * c)
    i = i + 1
print(s)