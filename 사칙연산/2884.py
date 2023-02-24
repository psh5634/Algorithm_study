h, m = map(int, input().split())

if h == 0:
    if m >= 45:
        print(h, m-45)
    elif m < 45:
        h = 23
        print(h, m+15)
    
elif m >= 45:
    print(h-0, m-45)

elif m < 45:
    print(h-1, m+15)