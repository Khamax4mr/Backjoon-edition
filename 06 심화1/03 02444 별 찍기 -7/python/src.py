from sys import exit

# 별 층 n 입력.
n = int(input())
if n < 1 or n > 100: exit(0)

for i in range(1, n):
    print(f"{' ' * (n-i)}{'*' * (2*i-1)}")
for i in range(n, 0, -1):
    print(f"{' ' * (n-i)}{'*' * (2*i-1)}")