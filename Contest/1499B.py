# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 21:32:25 2021

@author: Aspire
"""

t = int(input())

while(t):
    s = input()
    if '0' in s and '1' in s:
        i = 0
        f = 1
        oz = '1'
        while(i<len(s)-1):
            if s[i]==oz and s[i+1]==oz:
                if oz == '0':
                    f = 0
                    break
                oz = '0'
            else:
                f = 1
                
            i = i + 1
        if f==0:
            print('NO')
        else:
            print('YES')
    else:
        print('YES')
    
    t = t - 1

