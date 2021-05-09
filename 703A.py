# -*- coding: utf-8 -*-
"""
Created on Sun May  9 16:31:00 2021

@author: Aspire
"""

n = int(input())
x = 0
y = 0
for i in range(0,n):
    a,b = map(int,input().split())
    if a>b:
        x = x + 1
    elif b>a:
        y = y + 1

if x>y:
    print("Mishka")
elif y>x:
    print("Chris")
else:
    print("Friendship is magic!^^")