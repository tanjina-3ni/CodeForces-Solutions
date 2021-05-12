# -*- coding: utf-8 -*-
"""
Created on Wed May 12 10:18:25 2021

@author: Aspire
"""

i = 2
l = []
while i <= 30:
    g1 = 2**i
    g2 = 0
    j = 1
    while j < i:
        if j < i/2:
            g1 += 2**j
        else:
            g2 += 2**j
        j += 1
    l.append(abs(g1-g2))
    i += 2

t = int(input())
for i in range(0, t):
    n = int(input())
    print(l[int(n/2)-1])
