# -*- coding: utf-8 -*-
"""
Created on Wed May 12 12:44:32 2021

@author: Aspire
"""

n = input()
if int(n) >= 0:
    print(int(n))
elif n[len(n)-1] >= n[len(n)-2]:
    print(int(n[:-1]))
else:
    print(int(n[:-2]+n[len(n)-1]))