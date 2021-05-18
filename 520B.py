# -*- coding: utf-8 -*-
"""
Created on Tue May 18 19:46:22 2021

@author: Aspire
"""
def fun(n,m):
    if n>m:
        return n-m
    if n==m:
        return 0
    elif m%2 == 0:
        return 1+fun(n, int(m/2))
    else:
        return 1+fun(n, m+1)

n,m = map(int,input().split())

print(fun(n,m))

