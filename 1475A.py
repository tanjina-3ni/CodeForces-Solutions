# -*- coding: utf-8 -*-
"""
Created on Wed May 26 23:07:56 2021

@author: Aspire
"""

t = int(input())

for i in range(0,t):
    n = int(input())
    while n%2 == 0:
        n = int(n/2)
    if n==1:
        print('NO')
    else:
        print('YES')
    
    