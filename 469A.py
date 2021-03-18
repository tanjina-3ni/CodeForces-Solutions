# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 17:23:52 2021

@author: Aspire
"""

n = int(input())

x = list(map(int,input().split()))
y = list(map(int,input().split()))

f = (x[:0]+x[1:]) + (y[:0]+y[1:])
#print(f)
c = 0
for i in range(1,n+1):
    if i not in f:
        c = 1
        break
    
if c==1:
    print('Oh, my keyboard!')
else:
    print('I become the guy.')