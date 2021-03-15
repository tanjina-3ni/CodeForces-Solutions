# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 23:48:53 2021

@author: Aspire
"""
n = []
for i in range(0,3):
    n.append(int(input()))
if n[0]==1:
    x = (n[0] + n[1])
    if n[2] == 1:
        x = x + n[2]
    else:
        x = x * n[2]
        
        
elif n[1]==1:
    if n[0]<n[2]:
        x = (n[0] + n[1]) * n[2]
    else:
        x = (n[2] + n[1]) * n[0]

elif n[2] == 1:
    x = n[0] * (n[1] + n[2])
        
else:
    x = n[0] * n[1] * n[2] 
    
print(x)