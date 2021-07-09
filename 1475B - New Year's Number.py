def check(n):
    if n<2020:
        return 0
    if n%2020==0 or n%2021==0:
        return 1
    else:
        return check(n-2021)
    

t = int(input())
for i in range(t):
    n = int(input())
    res = check(n)
    if res==1:
        print('YES')
    else:
        print('NO')