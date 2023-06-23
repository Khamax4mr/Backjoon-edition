from sys import exit, stdin

# 제출 번호 n 입력.
n = [int(line.rstrip()) for line in stdin.readlines()]
if True in [not 1 <= submit <= 30 for submit in n]: exit()

# 제출 여부 구성.
for i in range(1, 31):
    if i in n: continue
    print(i)