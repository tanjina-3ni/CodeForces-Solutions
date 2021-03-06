# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 20:37:45 2021

@author: Aspire
"""

n = input()
output = []
one = 0
two = 0
three = 0

for i in range(0,len(n)):
    if n[i]=='1':
        one = one + 1
    if n[i]=='2':
        two = two + 1
    if n[i]=='3':
        three = three + 1


if one != 0 :
    for i in range(0,one):
        if two == 0 and three == 0 and i == one-1:
            output.append("1")
            break
        output.append("1+")
if two != 0:
    for i in range(0,two):
        if three == 0 and i == two-1:
            output.append("2")
            break
        output.append("2+")
if three != 0:
    for i in range(0,three):
        if i == three-1:
            output.append("3")
            break
        output.append("3+")
print(''.join(output))
