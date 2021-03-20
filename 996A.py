# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 22:15:49 2021

@author: Aspire
"""

dollar = [100,20,10,5,1]

n = int(input())

c = 0
i = 0
while(n):
    if n>=dollar[i]:
        c = c + int(n/dollar[i])
        
        n = n % dollar[i]
        
    i = i + 1
print(c)  
    