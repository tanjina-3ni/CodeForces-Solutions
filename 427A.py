# -*- coding: utf-8 -*-
"""
Created on Sat May  8 22:41:57 2021

@author: Aspire
"""

n = int(input())

l = list(map(int,input().split()))

officer = 0
crime = 0

for i in range(0,len(l)):
    if l[i] == -1 and officer == 0:
        crime = crime + 1
    elif l[i] == -1:
        officer = officer - 1
    else:
        officer = officer + l[i]
print(crime)
        