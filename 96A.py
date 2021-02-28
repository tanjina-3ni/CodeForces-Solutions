# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 21:12:50 2021

@author: Aspire
"""

count = 1
x = input()
for i in range(1,len(x)):
    if x[i] == x[i-1]:
        count = count + 1
        if count >= 7:
            break
    else:
        count = 1
if count == 7:
    print('YES')            
else:
    print('NO')
            
    