# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 16:10:52 2021

@author: Aspire
"""

sp = input().split()
s = int(sp[0])
p = int(sp[1])

puzzles = list(map(int,input().split()))

puzzles.sort()

res = 99999999999
x = s
i = 0
while(1):
    t = puzzles[x-1] - puzzles[i]
    if t<res:
        res = t

    x = x + 1
    i = i + 1
    if x > p:
        break
print(res)
    