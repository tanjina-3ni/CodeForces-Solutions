# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 11:08:40 2021

@author: Aspire
"""
import math
n = int(input())
while(n):
    ab = list(map(int, input().split()))
    if(ab[0]<ab[1]):
        print(ab[1]-ab[0])
    else:
        print(math.ceil(ab[0]/ab[1])*ab[1]-ab[0])
    n = n - 1