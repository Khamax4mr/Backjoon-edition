# 정수 a, b, c, d, e, f 입력.
a, b, c, d, e, f = map(int, input().split())
assert -999 <= a <= 999
assert -999 <= b <= 999
assert -999 <= c <= 999
assert -999 <= d <= 999
assert -999 <= e <= 999
assert -999 <= f <= 999

assert not a*e - b*d == 0
x = int((e*c - b*f) / (a*e - b*d))
y = int((a*f - d*c) / (a*e - b*d))
print(x, y)