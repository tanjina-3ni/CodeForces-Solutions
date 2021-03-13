# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 16:59:13 2021

@author: Aspire
"""

n = int(input())

s = input().split()

l = ''

for i in range(0,n):
    l = l + str((s.index(str(i+1))+1)) + ' '

print(l)