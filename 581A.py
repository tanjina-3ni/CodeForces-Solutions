# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 14:12:40 2021

@author: Aspire
"""
r,b = map(int,input().split())
x = min(r,b)
y = int((max(r,b) - x)/2)

print(x,y)