# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 20:22:24 2021

@author: Aspire
"""

for i in range(0,5):
    m = input().split()
    if '1' in m:
        r = i
        if m[0]=='1':
            c = 0
        elif m[1]=='1':
            c = 1
        elif m[2]=='1':
            c =2
        elif m[3]=='1':
            c = 3
        elif m[4]=='1':
            c = 4
print(abs(2-r)+abs(2-c))
    
    