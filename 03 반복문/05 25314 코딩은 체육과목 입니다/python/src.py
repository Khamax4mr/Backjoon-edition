from sys import exit

# 용량 n 입력.
n = int(input())
if n < 4 or n > 1000 or n % 4: exit(0)

# 출력.
print('long ' * (n // 4) + 'int')
