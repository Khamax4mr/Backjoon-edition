from sys import exit

# 최대 줄 n 입력.
n = int(input())
if n < 1 or n > 100: exit(0)

for i in range(n):
    print(f"{' ' * (n - (i+1))}{'*' * (i+1)}")