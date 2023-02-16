n,x = map(int, input().split())
my_list = list(map(int, input().split()))

for i in range(n):
    if x > my_list[i]:
        print(my_list[i], end=' ')