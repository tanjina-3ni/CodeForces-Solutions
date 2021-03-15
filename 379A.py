# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 23:40:46 2021

@author: Aspire
"""

n = list(map(int,input().split()))

a = n[0]
b = n[1]

res = a

while a >= b:
    res = res + int(a/b)
    a = int(a/b) + (a%b)

print(res)