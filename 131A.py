# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 21:44:30 2021

@author: Aspire
"""

lower = 'abcdefghijklmnopqrstuvwxyz'

n = input()
n1 = n[:0] + '' + n[1:]
if n.isupper():
    n = n.lower()
elif n[0] in lower:
    if n1.isupper():
        #print(n1)
        n1 = n1.lower()
        n = n[0].upper() + n1
        #print(n)
    elif n1=='':
        #print(n1)
        n = n.upper()


print(n)