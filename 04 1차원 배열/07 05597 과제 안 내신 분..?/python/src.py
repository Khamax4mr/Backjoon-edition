# 제출 번호 n 입력.
n = tuple(int(input()) for _ in range(28))
assert not False in [1 <= submit <= 30 for submit in n]

# 제출 여부 구성.
for i in range(1, 31):
    if i in n: continue
    print(i)