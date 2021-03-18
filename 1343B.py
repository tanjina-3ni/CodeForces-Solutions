# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 15:30:54 2021

@author: Aspire
"""

tc = int(input())
for i in range(0,tc):
    f = []
    l = []
    n = int(input())
    x = n/2
    if x%2 !=0:
        print('NO')
    else:
        print('YES')
        sum1 = int(x*(x+1))
        
        j = 2
        while(j <= n):
            f.append(j)
            j = j + 2
            
        i = 1
        sum2 = 0
        while(i <= n-2):
            l.append(i)
            sum2 = sum2 + i
            i = i + 2
        l.append(sum1-sum2)
        print(*(f+l), sep=' ')
