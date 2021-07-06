t = int(input())
for i in range(t):
    a,b,c,n = map(int,input().split())
    
    if (a+b+c+n)%3 != 0:
        print('NO')
    elif a > int((a+b+c+n)/3) or b > int((a+b+c+n)/3) or c > int((a+b+c+n)/3):
        print('NO')
    else:
        print('YES')