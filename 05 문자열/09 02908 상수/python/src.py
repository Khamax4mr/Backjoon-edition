from sys import exit

# 숫자 a, b 입력.
a, b = input().split()
if not a.isdigit(): exit()
if not b.isdigit(): exit()

# 정방향 숫자 구성.
number_a, number_b = int(a), int(b)
if not 100 <= number_a <= 1000: exit()
if not 100 <= number_b <= 1000: exit()

# 뒤집힌 숫자 구성.
reversed_a, reversed_b = int(a[::-1]), int(b[::-1])
print(reversed_a if reversed_a > reversed_b else reversed_b)