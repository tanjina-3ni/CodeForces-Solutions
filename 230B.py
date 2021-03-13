# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 17:26:43 2021

@author: Aspire
"""
import math

n = int(input())
s = list(map(int, input().split()))
for i in range(0, n):
    a = s[i]
    c = 0
    r = int(math.sqrt(a))
    if r*r != a or a == 1:
        print('NO')
    else:
        rr = int(math.sqrt(r))
        for j in range(2, rr+1):
            if r%j == 0:
                c = 1
        if c == 1:
            print('NO')
            c = 0
        else:
            print('YES')
