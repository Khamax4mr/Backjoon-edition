from sys import exit

# 숫자 n, 진법 b 입력.
n, b = map(int, input().split())
if not 0 < n <= 1000000000: exit()
if not 2 <= b <= 36: exit()

numberings = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
converted_n = ''
while n > 0:
    converted_n += numberings[n % b]
    n = n // b

print(converted_n[::-1])