li = []

for i in range(9):
    n = int(input())
    li.append(n)
find = max(li)
result = li.index(find)
print(max(li))
print(result+1)