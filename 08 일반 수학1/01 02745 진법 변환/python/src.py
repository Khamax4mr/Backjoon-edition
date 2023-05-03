from sys import exit

# 숫자 n, 진법 b 입력.
testcase = input().split()
n, b = testcase[0], int(testcase[1])
if b < 2 or b > 36: exit(0)

numberings = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
decimal_n = 0
for i in range(len(n)):
    decimal_n += numberings.index(n[i]) * b**(len(n) - i-1)

if decimal_n > 1000000000: exit(0)
print(decimal_n)