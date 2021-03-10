# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 13:31:26 2021

@author: Aspire
"""

n = int(input())

s = input()

A = s.count('A')

if A == (n - A):
    print('Friendship')
elif A > (n - A):
    print('Anton')
else:
    print('Danik')
    