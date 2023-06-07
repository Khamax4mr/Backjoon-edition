from sys import exit

# 정수 a, b, c, d, e, f 입력.
a, b, c, d, e, f = map(int, input().split())
if a < -999 or a > 999: exit(0)
if b < -999 or b > 999: exit(0)
if c < -999 or c > 999: exit(0)
if d < -999 or d > 999: exit(0)
if e < -999 or e > 999: exit(0)
if f < -999 or f > 999: exit(0)

if a*e - b*d == 0: exit(0)
x = int((e*c - b*f) / (a*e - b*d))
y = int((a*f - d*c) / (a*e - b*d))
print(x, y)