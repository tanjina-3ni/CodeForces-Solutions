def calculate(n):
    if n<10:
        return n
    nl = len(str(n))
    #print(nl)
    return (9*(nl-1)) + n//int("1"*nl)

t = int(input())
for i in range(t):
    n = int(input())
    print(calculate(n))
    