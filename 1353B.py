# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 11:23:55 2021

@author: Aspire
"""

t = int(input())

while(t):
    nk = list(map(int,input().split()))
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort(reverse=True)
    i = 0
    while(nk[1]):
        if a[i] >= b[i]:
            break
        else:
           a[i] = b[i]
           i = i + 1
        nk[1] = nk[1] - 1
    print(sum(a))
    
    t = t - 1