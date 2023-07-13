# 시간 a, b, c 입력.
a, b = map(int, input().split())
c = int(input())
assert 0 <= a <= 23
assert 0 <= b <= 59
assert 0 <= c <= 1000

# 시간 계산.
cooking_h, cooking_m = c//60, c%60
carry = (b + cooking_m) // 60
b = (b + cooking_m) % 60
a = (a + cooking_h + carry) % 24
print(a, b)