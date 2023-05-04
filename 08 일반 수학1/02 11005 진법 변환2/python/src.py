from sys import exit

# 숫자 n, 진법 b 입력.
n, b = map(int, input().split())
if n <= 0 or n > 1000000000: exit(0)
if b < 2 or b > 36: exit(0)

numberings = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
converted_n = ''
while n > 0:
    converted_n = numberings[n % b] + converted_n
    n = n // b

print(converted_n)