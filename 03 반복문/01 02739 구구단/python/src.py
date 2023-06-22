from sys import exit

# 숫자 n단 입력.
n = int(input())
if not 1 <= n <= 9: exit()

for i in range(1, 10):
    print(f'{n} * {i} = {n * i}')