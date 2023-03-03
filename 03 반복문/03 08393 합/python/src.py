from sys import exit

# 숫자 n 입력.
n = int(input())
if n < 1 or n > 10000: exit(0)

# 출력.
print(sum(range(n + 1)))