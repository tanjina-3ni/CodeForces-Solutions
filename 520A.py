# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 16:51:22 2021

@author: Aspire
"""

a = set('abcdefghijklmnopqrstuvwxyz')
l = int(input())
s = input()
c = 0


s = set(s.lower())
#print(a,s)

if s == a:
    print('YES')
else:
    print('NO')