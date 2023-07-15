import string

# 숫자 범위 설정.
numberings = string.digits + string.ascii_uppercase

# 숫자 n, 진법 b 입력.
n, b = map(str, input().split())
b = int(b)
assert 2 <= b <= 36
assert not False in [a in numberings[:b] for a in n]

decimal_n = sum((numberings.index(n[i]) * b**(len(n) - i-1) for i in range(len(n))))
assert decimal_n <= 1000000000
print(decimal_n)