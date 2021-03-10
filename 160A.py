# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 23:44:49 2021

@author: Aspire
"""

n = int(input())

coin = list(map(int, input().split()))
coin.sort(reverse=True)

half = sum(coin)/2

s = 0
i = 0
c = 0

for i in range(0, n):
    if s <= half:
        c = c + 1
        s = s + coin[i]
    else:
        break
print(c)