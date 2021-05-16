# -*- coding: utf-8 -*-
"""
Created on Sun May 16 12:50:59 2021

@author: Aspire
"""

n = int(input())
l = ''
x = int(n/2)
for i in range(0,x-1):
    l = l + '2 '
if n%2 == 0:
    l = l + '2'
else:
    l = l + '3'
    
print(x)
print(l)