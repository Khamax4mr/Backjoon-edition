# 숫자 n단 입력.
n = int(input())
assert 1 <= n <= 9

for i in range(1, 10):
    print(f'{n} * {i} = {n * i}')