# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 23:18:59 2021

@author: Aspire
"""

s = input().split()

limak = int(s[0])
bob = int(s[1])

for i in range(0,10):
    limak = limak*3
    bob = bob*2
    if limak>bob:
        break

print(i+1)