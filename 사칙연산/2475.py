def cal(a,b,c,d,e):
    result = (a ** 2 + b ** 2 + c ** 2 + d ** 2 + e ** 2) % 10
    return result

a, b, c, d, e = map(int, input().split())
result = cal(a,b,c,d,e)
print(result)




li = list(map(int, input().split()))
result = 0
for i in range(5):
    result += li[i] ** 2
print(result % 10)