from sys import exit, stdin, stdout

# 점 개수 n 입력.
n = int(input())
if n < 1 or n > 100000: exit(0)

dots = []
for _ in range(n):
    x, y = map(int, stdin.readline().rstrip().split())
    if x < -100000 or x > 100000: exit(0)
    if y < -100000 or y > 100000: exit(0)
    dots.append((x, y))

dots.sort(key=lambda x : (x[1], x[0]))
stdout.write('\n'.join([' '.join(map(str, dot)) for dot in dots]))