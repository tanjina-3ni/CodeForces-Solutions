# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 22:28:29 2021

@author: Aspire
"""


inp = input().split()
#print(inp)

n = int(inp[0])
m = int(inp[1])
a = int(inp[2])

i = int(n/a)
j = int(m/a)
if i*a != n:
    i=i+1
if j*a !=m:
    j=j+1
print(i*j)