def cal(a,b):
    result = (a+b)*(a-b)
    return result

a, b = map(int, input().split())
result = cal(a,b)
print(result)