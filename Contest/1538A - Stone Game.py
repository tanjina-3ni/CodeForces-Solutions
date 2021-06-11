t = int(input())
for i in range(0,t):
    n = int(input())
    a = list(map(int,input().split()))
    min_l = a.index(min(a))
    min_r = len(a)-1-min_l
    max_l = a.index(max(a))
    max_r = len(a)-1-max_l
    step = min(min_l,min_r,max_l,max_r)+1
    if step-1 == min_l:
        del a[:step]
       # print(a,1)
        step = step + min(a.index(max(a)), len(a)-1-a.index(max(a)))+1
       # print(a.index(max(a)), len(a)-1-a.index(max(a)))
        
    elif step-1 == max_l:
        del a[:step]
       # print(a,2)
        step = step + min(a.index(min(a)), len(a)-1-a.index(min(a)))+1
       # print(a.index(min(a)), len(a)-1-a.index(min(a)))
        
    elif step-1 == max_r:
        del a[-(step):]
        #print(a,3)
        step = step + min(a.index(min(a)), len(a)-1-a.index(min(a)))+1
        #print(a.index(min(a)), len(a)-1-a.index(min(a)))
        
    else:
        del a[-(step):]
        #print(a,4)
        step = step + min(a.index(max(a)), len(a)-1-a.index(max(a))) +1
        #print(a.index(max(a)), len(a)-1-a.index(max(a)))
    print(step) 
    
    
             