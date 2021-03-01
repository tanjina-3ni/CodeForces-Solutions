# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 20:32:57 2021

@author: Aspire
"""

n = int(input())
count = 0

for i in range(0,n):
    x = 0
    y = 0
    inp = input().split()
    for char in inp:
        if char=='1':
            x = x + 1
        else:
            
            y = y + 1
    if x>y:
        count = count+1
            
print(count)

        
        
    

