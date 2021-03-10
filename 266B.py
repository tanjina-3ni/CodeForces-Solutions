# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 19:28:01 2021

@author: Aspire
"""

nt = input().split()

n = int(nt[0])
t = int(nt[1])

s = input()
# s = s[:2-1]+'B'+'G'+s[2+1:]
for j in range(0,t):
    i = 1
    while(i<n):
        if s[i-1]=='B' and s[i]=='G':
            s = s[:i-1]+'G'+'B'+s[i+1:]
        
            i = i+1
        i = i+1

print(s)