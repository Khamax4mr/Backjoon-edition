from sys import exit

# 숫자 a, b 입력.
a, b = input().split()
number_a, number_b = int(a), int(b)
if number_a < 100 or number_a >= 1000: exit(0)
if number_b < 100 or number_b >= 1000: exit(0)

# 뒤집힌 숫자 구성.
reversed_a, reversed_b = int(a[::-1]), int(b[::-1])
print(reversed_a if reversed_a > reversed_b else reversed_b)