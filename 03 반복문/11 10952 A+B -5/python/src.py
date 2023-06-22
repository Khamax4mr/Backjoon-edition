from sys import exit, stdin

for line in stdin.readlines()[:-1]:
    # 숫자 a, b 입력.
    a, b = map(int, line.rstrip().split())
    if not 0 < a < 10: exit()
    if not 0 < b < 10: exit()

    print(a + b)