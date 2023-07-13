# 용량 n 입력.
n = int(input())
assert 4 <= n <= 1000 or n % 4

print(f"{'long ' * (n // 4)}int")