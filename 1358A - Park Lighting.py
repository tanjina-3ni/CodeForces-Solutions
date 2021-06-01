# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 16:32:36 2021

@author: Aspire
"""
import math
t = int(input())
for i in range(0,t):
    n,m = map(int,input().split())
    print(math.ceil(n*m/2))