# -*- coding: utf-8 -*-
"""
Created on Wed May 12 12:33:55 2021

@author: Aspire
"""

t = int(input())

for i in range(0, t):
    n = int(input())
    k = 2
    while 1:
        if n%(2**k - 1) == 0:
            print(int(n/(2**k - 1)))
            break
        k += 1