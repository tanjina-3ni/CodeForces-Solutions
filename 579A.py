# -*- coding: utf-8 -*-
"""
Created on Wed May 12 13:01:02 2021

@author: Aspire
"""

x = int(input())
b = 0
while x:
    b += x%2
    x = int(x/2)
print(b)