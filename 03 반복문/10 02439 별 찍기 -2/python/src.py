# 최대 줄 n 입력.
n = int(input())
assert 1 <= n <= 100

for i in range(n):
    print(f"{' ' * (n - (i+1))}{'*' * (i+1)}")