# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 21:10:03 2021

@author: Aspire
"""
t = int(input())

for i in range(0,t):
    nk1k2 = list(map(int,input().split()))
    wb = list(map(int,input().split()))
    
    bl = nk1k2[0] - max(nk1k2[1],nk1k2[2])
    wh = min(nk1k2[1],nk1k2[2])
    diff = nk1k2[0]-(bl+wh)
    
    if wh + int(diff/2)>=wb[0] and bl + int(diff/2)>=wb[1]:
        print('YES')
    else:
        print('NO')
        
