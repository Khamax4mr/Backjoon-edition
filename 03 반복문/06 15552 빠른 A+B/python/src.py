from sys import exit, stdin

# 테스트케이스 개수 t 입력.
t = int(stdin.readline().rstrip())
if t < 0 or t > 1000000: exit(0)

for i in range(t):
    # 숫자 a, b 입력.
    a, b = map(int, stdin.readline().rstrip().split())
    if a < 1 or a > 1000: exit(0)
    if b < 1 or b > 1000: exit(0)

    print(a + b)