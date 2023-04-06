from sys import exit

# 숫자 a, b, c 입력.
a, b, c = map(int, input().split())
if a < 2 or a > 10000: exit()
if b < 2 or b > 10000: exit()
if c < 2 or c > 10000: exit()

print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)