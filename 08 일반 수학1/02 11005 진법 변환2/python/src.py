import string

# 숫자 범위 설정.
numberings = string.digits + string.ascii_uppercase

# 숫자 n, 진법 b 입력.
n, b = map(int, input().split())
assert 0 < n <= 1000000000
assert 2 <= b <= 36

converted_n = ''
while n > 0:
    converted_n += numberings[n % b]
    n = n // b

print(converted_n[::-1])