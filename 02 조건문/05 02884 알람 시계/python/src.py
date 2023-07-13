# 시간 h, m 입력.
h, m = map(int, input().split())
assert 0 <= h <= 23
assert 0 <= m <= 60

# 시간 계산.
h = (h+23) % 24 if m < 45 else h
m = (m+15) % 60
print(h, m)