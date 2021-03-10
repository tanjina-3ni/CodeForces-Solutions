# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 17:02:38 2021

@author: Aspire
"""

n = int(input())
f = 0
lucky = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]        
if n in lucky:
    print('YES')
else:
    for i in range(0,len(lucky)):
        if n%lucky[i]==0:
            f=1
    if f==1:
        print('YES')
    else:
        print('NO')
            
    
