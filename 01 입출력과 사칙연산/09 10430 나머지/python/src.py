from sys import exit

# 숫자 a, b, c 입력.
a, b, c = map(int, input().split())
if not 2 <= a <= 10000: exit()
if not 2 <= b <= 10000: exit()
if not 2 <= c <= 10000: exit()

print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)