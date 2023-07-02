from sys import exit

# 정수 a, b, c, d, e, f 입력.
a, b, c, d, e, f = map(int, input().split())
if not -999 <= a <= 999: exit()
if not -999 <= b <= 999: exit()
if not -999 <= c <= 999: exit()
if not -999 <= d <= 999: exit()
if not -999 <= e <= 999: exit()
if not -999 <= f <= 999: exit()

if a*e - b*d == 0: exit()
x = int((e*c - b*f) / (a*e - b*d))
y = int((a*f - d*c) / (a*e - b*d))
print(x, y)