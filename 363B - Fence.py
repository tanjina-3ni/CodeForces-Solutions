n,k = map(int,input().split())
h = list(map(int,input().split()))

summ = sum(h[:k])
temp_sum = summ

indx = 0
for i in range(0,n-k):
    
    temp_sum = temp_sum + h[k + i] - h[i]
    #print(summ,temp_sum,i, h[k + i],h[i])
    if temp_sum<summ:
        summ = temp_sum
        indx = i+1
        #print(summ,temp_sum,indx)
   
    
print(indx+1)