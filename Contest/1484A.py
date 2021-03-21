# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 19:28:09 2021

@author: Aspire
"""

t = int(input())

for i in range(0,t):
    ab = list(map(int,input().split()))
    print(ab[0]*ab[1])