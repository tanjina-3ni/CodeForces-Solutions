# -*- coding: utf-8 -*-
"""
Created on Sun May 16 13:05:38 2021

@author: Aspire
"""

n = int(input())
a = list(map(int,input().split()))
a.sort()
m = int(input())
b = list(map(int,input().split()))
b.sort()
c = 0
i = 0
j = 0
while len(a)!=0 and len(b)!=0:
    #print(a, b, i, j)
    if abs(a[i]-b[j])<=1:
        a.remove(a[i])
        b.remove(b[j])
        i = 0
        j = 0
        c = c + 1
        continue
    if a[i]-b[j]>1:
        j = j + 1
    else:
        i = i + 1
    if i>=len(a) or j>=len(b):
        break
    
print(c)           