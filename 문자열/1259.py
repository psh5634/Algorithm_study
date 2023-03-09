while True:
   n = input()
   if (n == '0'):
      break
   else:
      flag = 'yes'
      for i in range(len(n) // 2):
         if n[0 + i] != n[-1 - i]:
            flag = 'no'
            break
      print(flag)