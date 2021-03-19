# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 21:24:25 2021

@author: Aspire
"""

a = list(input())
b = list(input())
c = list(input())

d = (a+b)
d.sort()
c.sort()
if d==c:
    print('YES')
else:
    print('NO')
