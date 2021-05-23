# -*- coding: utf-8 -*-
"""
Created on Sun May 23 22:44:17 2021

@author: Aspire
"""
c = 0

def check(n,c):
    if n==1:
        print(c)
        return
    elif n%6==0:
        c = c + 1
        check(int(n/6),c)
    else:
        if (n*2%3)==0:
            c = c + 1
            check(n*2,c)
        else:
            print(-1)
            return


t = int(input())
for i in range(0,t):
    n = int(input())
    check(n,c)