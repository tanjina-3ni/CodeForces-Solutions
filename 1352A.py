# -*- coding: utf-8 -*-
"""
Created on Tue May  4 14:05:15 2021

@author: Aspire
"""

t = int(input())

for i in range(0,t):
    n = input()
    l = len(n)
    lst = ''
    c = 0
    for j in range(0,l):
        if n[j]!='0':
            lst = lst + str((int(n[j])*10**(l-j-1)))+ ' ' 
            c = c + 1
    print(c)
    print(lst)