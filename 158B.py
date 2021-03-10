# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 21:02:18 2021

@author: Aspire
"""

n = int(input())

s = input().split()
for i in range(0,len(s)):
    s[i] = int(s[i])
    
s.sort(reverse=True)
#print(s)

i = 0
c = 0

while(i < n):
    if s[i] == 4:
        c = c + 1
        #print('l1 ',c)
    elif s[i] == 3 and s[n-1] == 1:
        c = c + 1
        #print('l2 ',c)
        n = n - 1
    elif s[i] == 3:
        c = c + 1
        #print('l3 ',c)
    
    else:
        summ = 0
        while(i<n):
            
            summ = summ + s[i]
            if summ == 4:
                c = c + 1
                #print('l4 ',c)
                break
            if i == n-1:
                c = c + 1
               # print('l5 ',c)
                break
            i = i + 1
          
        
    i = i + 1
print(c)  