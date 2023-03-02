n = int(input())

li = list(map(int, input().split()))

print(min(li), end=' ')
print(max(li))



min = 1000000
max = -1000000
n = int(input())
li = list(map(int, input().split()))

for i in li:
    if i > max:
        max = i
    if i < min:
        min = i
        
print(min, max)