from sys import exit

# 용량 n 입력.
n = int(input())
if not 4 <= n <= 1000 or n % 4: exit()

print(f"{'long ' * (n // 4)}int")