# 숫자 a, b 입력.
a, b = input().split()
assert a.isdigit()
assert b.isdigit()

# 정방향 숫자 구성.
number_a, number_b = int(a), int(b)
assert 100 <= number_a <= 1000
assert 100 <= number_b <= 1000

# 뒤집힌 숫자 구성.
reversed_a, reversed_b = int(a[::-1]), int(b[::-1])
print(reversed_a if reversed_a > reversed_b else reversed_b)