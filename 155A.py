# -*- coding: utf-8 -*-
"""
Created on Mon May  3 15:45:38 2021

@author: Aspire
"""

t = input()
n = list(map(int,input().split()))

c = 0

i = 1
maxx = n[0]
minn = n[0]
while(i<int(t)):
    if n[i]>maxx:
        maxx = n[i]
        c = c + 1
    elif n[i]<minn:
        minn = n[i]
        c = c + 1
    i = i + 1
print(c)