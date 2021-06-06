def divide(w,h):
    global c
    if w%2 == 0:
        c *= 2
        w = int(w/2)
        #print(w,h)
        divide(w,h)
    elif h%2 == 0:
        c *= 2
        h = int(h/2)
        #print(w,h)
        divide(w,h)
    else:
        return 

t = int(input())
for i in range(0,t):
    c = 1
    w,h,n = map(int, input().split())
    divide(w,h)
    #print(c)
    if c<n:
        print('NO')
    else:
        print('YES')
        