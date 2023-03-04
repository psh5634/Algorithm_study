T = int(input())

for i in range(T):
    result = 0
    score = 1
    s = input()
    for j in s:
        if j == 'O':
            result += score
            score += 1
        elif j == 'X':
            score = 1
    print(result)
            