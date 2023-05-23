from sys import exit

# 가장 아랫부분의 정사각형 개수 n 입력.
n = int(input())
if n < 1 or n > 10**9: exit(0)

print(n * 4)