# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 10:07:57 2021

@author: Aspire
"""

n,m = map(int,input().split())

s1 = '#'*m
s2 = '.'*(m-1)
f = 1
for i in range(0,n):
    if i%2==0:
        print(s1)
    else:
        if f:
            print(s2+'#')
        
        else:
            print('#'+s2)
        f = not f
        
