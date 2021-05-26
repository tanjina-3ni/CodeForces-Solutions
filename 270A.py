# -*- coding: utf-8 -*-
"""
Created on Wed May 26 23:08:58 2021

@author: Aspire
"""


t = int(input())

for i in range(0,t):
    a = int(input())
    if not (360%(180-a)):
        print('YES')
    else:
        print('NO')