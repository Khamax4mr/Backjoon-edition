from sys import exit, stdin, stdout

# 테스트케이스 개수 t 입력.
t = int(stdin.readline().rstrip())
if not 0 < t <= 1000000: exit()

sum = []
for _ in range(t):
    # 숫자 a, b 입력.
    line = stdin.readline().rstrip()
    a, b = map(int, line.split())
    if not 1 <= a <= 1000: exit()
    if not 1 <= b <= 1000: exit()

    sum.append(a + b)

stdout.write('\n'.join(map(str, sum)))