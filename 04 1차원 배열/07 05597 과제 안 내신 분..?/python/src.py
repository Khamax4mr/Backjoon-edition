from sys import exit

# 제출 번호 n 입력.
n = [int(input()) for _ in range(28)]
if True in [submit < 1 or submit > 30 for submit in n]: exit(0)

# 제출 여부 구성.
for i in range(1, 31):
    if i in n: continue
    print(i)