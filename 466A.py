# -*- coding: utf-8 -*-
"""
Created on Tue May  4 14:33:29 2021

@author: Aspire
"""

n,m,a,b = map(int,input().split())

if n<=m and n*a>b:
    print(b)
elif n>m and n*a>int(n/m)*b:
    if (n%m)*a>b:
        print(int(n/m)*b + b)
    else:
        print(int(n/m)*b + (n%m)*a)
else:
    print(n*a)
        