# -*- coding: utf-8 -*-
"""
Created on Mon May 24 11:31:57 2021

@author: Aspire
"""

t = int(input())
for i in range(0,t):
    n = input()
    l = len(n)
    s = (int(n[0])-1)*10 + int((l * (l+1))/2)
    print(s)
