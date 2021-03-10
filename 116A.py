# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 19:31:28 2021

@author: Aspire
"""

stopage = int(input())
maximum = 0
res = 0
for i in range(0,stopage):
    passenger = input().split()
    p_in = int(passenger[1])
    p_out = int(passenger[0])
    
    res = res + p_in - p_out
   
    if res>maximum:
        maximum = res
        
print(maximum)
    
    