from sys import exit
from string import digits, ascii_uppercase

# 숫자 범위 설정.
numberings = digits + ascii_uppercase

# 숫자 n, 진법 b 입력.
n, b = map(str, input().split())
b = int(b)
if not 2 <= b <= 36: exit()
if False in [a in numberings[:b] for a in n]: exit()

decimal_n = sum([numberings.index(n[i]) * b**(len(n) - i-1) for i in range(len(n))])
if decimal_n > 1000000000: exit()
print(decimal_n)