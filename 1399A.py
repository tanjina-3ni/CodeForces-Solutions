# -*- coding: utf-8 -*-
"""
Created on Mon May  3 12:33:09 2021

@author: Aspire
"""

t = int(input())
for i in range(0,t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    j = 1
    k = 0
    while(j<n):
        if a[j]-a[j-1]>1:
            k = 1
            break
        j = j + 1
        
    if k==1:
        print('NO')
    else:
        print('YES')
