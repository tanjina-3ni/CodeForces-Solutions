# -*- coding: utf-8 -*-
"""
Created on Sun May  9 10:52:26 2021

@author: Aspire
"""

n,k = map(int,input().split())

l = list(map(int,input().split()))
cc = 0
for i in range(0,(5-k)+1):
    c = l.count(i)
    cc = c + cc
    #print(i)
print(int(cc/3))
