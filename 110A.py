# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 23:33:50 2021

@author: Aspire
"""

n = input()

c = n.count('4')+n.count('7')

if c == 4 or c == 7:
    print('YES')
else:
    print('NO')