T = int(input())

for i in range(T):
    h, w, n = map(int, input().split())
    floor = n % h
    num = n // h
    if floor == 0:
        floor = h
    else:
        num += 1
    print(100 * floor + num)