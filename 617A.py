# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 20:42:49 2021

@author: Aspire
"""

x = int(input())

s = x % 5

if s == 0:
    m = int(x/5)
    print(m)
else:
    m = int((x/5)+1)
    print(m)
    