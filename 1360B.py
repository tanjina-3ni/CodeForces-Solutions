# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 19:26:54 2021

@author: Aspire
"""

t = int(input())

for i in range(0,t):
    n = int(input())
    s = list(map(int,input().split()))
    s.sort()
    ans = 9999
    for j in range(1,n):
        if (s[j]-s[j-1])<ans:
            ans = s[j]-s[j-1]
    
    print(ans)