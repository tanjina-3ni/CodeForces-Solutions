# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 11:23:11 2021

@author: Aspire
"""

def xor(a,b):
    l = []
    for i in range(0,len(a)):
        if a[i]!=b[i]:
            l.append('1')
        else:
            l.append('0')
    return l

a = input()
b = input()
l = xor(a,b)
l = ''.join(l)
print(l)
