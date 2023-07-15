# 별 층 n 입력.
n = int(input())
assert 1 <= n <= 100

for i in range(1, n):
    print(f"{' ' * (n-i)}{'*' * (2*i-1)}")
for i in range(n, 0, -1):
    print(f"{' ' * (n-i)}{'*' * (2*i-1)}")