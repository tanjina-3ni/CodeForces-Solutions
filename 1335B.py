# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 20:35:44 2021

@author: Aspire
"""

t = int(input())
alp = 'abcdefghijklmnopqrstuvwxyz'

for i in range(0,t):
    ans = ''
    nab = list(map(int,input().split()))
    
    if nab[1] == nab[2]:
        for i in range(0,nab[0]):
            ans = ans + alp[i%26]
    elif nab[2] == 1:
        for i in range(0,nab[0]):
            ans = ans + 't'
    else:
        i = 0
        while(i<nab[0]):
            ans = ans + alp[i%nab[2]]
            i = i + 1
            
    print(ans)