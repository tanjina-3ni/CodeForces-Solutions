# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 15:58:01 2021

@author: Aspire
"""

col = input()

cubes = list(map(int,input().split()))
cubes.sort()
cubes = ' '.join(map(str, cubes)) 
print(cubes)
