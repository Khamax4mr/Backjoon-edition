from sys import exit, stdin

# 점 개수 n 입력.
n = int(input())
if not 1 <= n <= 100000: exit()

dots = []
for _ in range(n):
    x, y = map(int, stdin.readline().rstrip().split())
    if not -100000 <= x <= 100000: exit()
    if not -100000 <= y <= 100000: exit()
    dots.append((x, y))

dots.sort()
print('\n'.join([' '.join(map(str, dot)) for dot in dots]))