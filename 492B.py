# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 19:40:49 2021

@author: Aspire
"""

n = list(map(int, input().split()))

l = n[1]

a = list(map(int, input().split()))

a.sort()

if a[0] > (n[1]-a[len(a)-1]):
    dist = a[0]
else:
    dist = n[1]-a[len(a)-1]

for i in range(1,n[0]):
    if (a[i]-a[i-1])/2 > dist:
        dist = (a[i]-a[i-1])/2
        
print("{:.10f}".format(dist))