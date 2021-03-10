# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 18:47:22 2021

@author: Aspire
"""

nk = input().split()
n = int(nk[0])
k = int(nk[1])

for i in range(0,k):
    
    if n%10 == 0:
        n = int(n/10)
    else:
        n = n-1
print(n)