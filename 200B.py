# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 15:20:16 2021

@author: Aspire
"""

n = int(input())

s = input().split()
summ = 0

for i in range(0,len(s)):
    summ = summ + int(s[i])
    
print("{:.12f}".format(summ/n))