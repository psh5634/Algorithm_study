T = int(input())

for i in range(T):
    r,s = map(str, input().split())
    r = int(r)
    for j in s:
        print(j*r, end='')
    print()