# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 22:09:14 2021

@author: Aspire
"""
import math
n = list(map(int,input().split()))
half = math.ceil(n[0]/2)
if n[1]<=half:
    print(n[1]*2-1)
else:
    print((n[1]-half)*2)