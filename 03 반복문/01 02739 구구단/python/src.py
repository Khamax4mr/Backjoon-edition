from sys import exit

# 숫자 n단 입력.
n = int(input())
if n < 1 or n > 9: exit(0)

# 출력.
for i in range(1, 10):
    print(f'{n} * {i} = {n * i}')