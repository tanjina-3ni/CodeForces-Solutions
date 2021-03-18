# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 23:46:01 2021

@author: Aspire
"""

k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
c = 0
while(d):
    if d%k==0 or d%l==0 or d%m==0 or d%n==0:
        c = c + 1
    d = d - 1
print(c)