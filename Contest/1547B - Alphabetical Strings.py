l = 'abcdefghijklmnopqrstuvwxyz'
t = int(input())
for i in range(t):
    n = input()
    s = ""
    x = 0
    k = 0
    f = 1
    while k<len(n):
        if l[k] not in n:
            f = 0
            break
        
        a = n.index(l[k])
        if a>x:
            x = a
            s = s + l[k]
        else:
            x = a
            s = l[k] + s
        k += 1
        
    if s==n:
        print("YES")
    else:
        print("NO")
        
        
        