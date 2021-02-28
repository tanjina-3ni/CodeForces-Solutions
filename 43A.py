# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 20:53:08 2021

@author: Aspire
"""
def most_frequent(List): 
    counter = 0
    num = List[0] 
      
    for i in List: 
        curr_frequency = List.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            num = i 
  
    return num

n = int(input())
r = []
for i in range(0,n):
    team = input()
    r.append(team)
    
    
res = most_frequent(r)

print(res)
    