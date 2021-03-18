# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 10:59:11 2021

@author: Aspire
"""

n = input()
n = set(n)
if len(n) < 4:
    print(len(n)-2)
else:
    print(len(n)-4)