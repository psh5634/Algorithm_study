s = input()

print(s.swapcase())





before = input()
after = ''
for i in before:
    temp = ord(i)
    if (65 <= temp <= 90):
        after += chr(temp + 32)
    elif (97 <= temp <= 122):
        after += chr(temp - 32)
print(after)