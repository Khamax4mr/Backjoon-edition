from sys import exit

# 최대 줄 n 입력.
n = int(input())
if n < 1 or n > 100: exit(0)

for i in range(1, n + 1):
    # 출력.
    print('*' * i)
