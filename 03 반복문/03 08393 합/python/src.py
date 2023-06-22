from sys import exit

# 숫자 n 입력.
n = int(input())
if not 1 <= n <= 10000: exit()

print(sum(range(n + 1)))