# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 20:17:14 2021

@author: Aspire
"""

t = int(input())
for i in range(0,t):
    n = int(input())
    if n%2 == 0:
        ans = int(n/2) - 1
    else:
        ans = int(n/2)
    print(ans)