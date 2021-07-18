t = int(input())
for i in range(t):
    k , n, m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    l = []
    for j in range(max(n,m)):
        if len(a)>j:
            if a[j]==0:
                k = k + 1
                l.append(a[j])
            elif (a[j]>0 and k>=a[j]):
                l.append(a[j])
        
        if len(b)>j:
            
            if b[j]==0:
                k = k + 1
                l.append(b[j])
            
            elif (b[j]>0 and k>=b[j]):
                l.append(b[j])
        print(l)
    if len(l)==n+m:
        print(l)
    else:
        print(-1)
            
            