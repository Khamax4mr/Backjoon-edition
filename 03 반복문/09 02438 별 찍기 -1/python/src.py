from sys import exit

# 최대 줄 n 입력.
n = int(input())
if not 1 <= n <= 100: exit()

for i in range(n):
    print('*' * (i+1))