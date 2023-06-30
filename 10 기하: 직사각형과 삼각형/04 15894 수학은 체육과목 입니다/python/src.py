from sys import exit

# 가장 아랫부분의 정사각형 개수 n 입력.
n = int(input())
if not 1 <= n <= 10**9: exit()

print(n * 4)