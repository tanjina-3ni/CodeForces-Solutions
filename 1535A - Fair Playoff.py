t = int(input())
for i in range(t):
    s = list(map(int,input().split()))
    
    a = sorted(s,reverse=True)
    m1 = s.index(a[0])
    m2 = s.index(a[1])
    
    if ((m1==0 or m1==1) and (m2==2 or m2==3)) or ((m2==0 or m2==1) and (m1==2 or m1==3)):
        print("YES")
    else:
        print("NO")
    

