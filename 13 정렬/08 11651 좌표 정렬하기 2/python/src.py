import sys
readline = sys.stdin.readline

# 점 개수 n 입력.
n = int(input())
assert 1 <= n <= 100000

dots = []
for _ in range(n):
    x, y = map(int, readline().rstrip().split())
    assert -100000 <= x <= 100000
    assert -100000 <= y <= 100000
    dots.append((x, y))

dots.sort(key=lambda x : (x[1], x[0]))
print('\n'.join(' '.join(map(str, dot)) for dot in dots))