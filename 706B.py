# -*- coding: utf-8 -*-
"""
Created on Sun May 16 09:55:03 2021

@author: Aspire
"""
import bisect
n = input()
x = list(map(int,input().split()))
x.sort()
#print(x)
q = int(input())

for i in range(0,q):
    c = 0
    j = 0
    l = len(x)
    m = int(input())
    print (bisect.bisect(x, m))
    #count = len([j for j in x if j > m])
    # while j<l:
    #     if x[j]<=m:
    #         c = c + 1
    #     else:
    #         break
    #     j = j + 1
    #print(c)
    