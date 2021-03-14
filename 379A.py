# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 23:40:46 2021

@author: Aspire
"""

n = list(map(int,input().split()))

a = n[0]
b = n[1]

def candles(a):
    if a == 0:
        return 0
    return a + candles(int(a/b))

print(candles(a))