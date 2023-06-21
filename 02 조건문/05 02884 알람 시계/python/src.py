from sys import exit

# 시간 h, m 입력.
h, m = map(int, input().split())
if not 0 <= h <= 23: exit()
if not 0 <= m <= 60: exit()

# 시간 계산.
h = (h+23) % 24 if m < 45 else h
m = (m+15) % 60
print(h, m)