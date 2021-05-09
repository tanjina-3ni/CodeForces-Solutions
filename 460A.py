# -*- coding: utf-8 -*-
"""
Created on Sun May  9 11:07:20 2021

@author: Aspire
"""

n,m = map(int,input().split())
x = n
while(x>1):
    x = x/m
    n = n + x
print(int(n))
    
    