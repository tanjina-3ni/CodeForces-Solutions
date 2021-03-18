# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 23:27:59 2021

@author: Aspire
"""

t = int(input())
h = []
g = []
while(t):
    hg = list(map(int, input().split()))
    h.append(hg[0])
    g.append(hg[1])
    t = t - 1
    
c = 0
for i in range(0, len(h)):
    for j in range(0, len(g)):
        if h[i] == g[j]:
            c = c + 1
print(c)