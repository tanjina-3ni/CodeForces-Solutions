t = int(input())
for i in range(0,t):
    n = int(input())
    a = list(map(int,input().split()))
    summ = sum(a)
    a = set(a)
    #print(a)
    if summ%2 != 0:
        print('NO')
    else:
        if n%2 !=0 and len(a)==1:
            print('NO')
        else:
            print('YES')