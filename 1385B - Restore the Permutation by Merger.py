# -*- coding: utf-8 -*-
"""
Created on Wed May 26 20:15:14 2021

@author: Aspire
"""

t = int(input())
for i in range(0,t):
    n = int(input())
    a = input().split()
    set_a = list(set(a))
    s = ''
    i = 0
    while len(set_a) != 0:
        if a[i] in set_a:
            s = s + a[i] + ' '
            set_a.remove(a[i])
        i = i + 1
    print(s)