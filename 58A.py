# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 20:38:47 2021

@author: Aspire
"""

s = input()

char = 'hello'
c = 0
for i in range(0,len(s)):
    if s[i] == char[c]:
       # print(char[c])
        c = c+1
       # print(c)
        if c==5:
           break
      
if c==5:
    print('YES')
else:
    print('NO')
    