from sys import exit

# 숫자 n, 진법 b 입력.
n, b = map(str, input().split())
b = int(b)
if not 2 <= b <= 36: exit()

numberings = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
decimal_n = sum([numberings.index(n[i]) * b**(len(n) - i-1) for i in range(len(n))])

if decimal_n > 1000000000: exit()
print(decimal_n)