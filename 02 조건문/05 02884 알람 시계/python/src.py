from sys import exit

# 시간 h, m 입력.
h, m = map(int, input().split())
if h < 0 or h > 23: exit(0)
if m < 0 or h > 59: exit(0)

# 시간 계산.
if m < 45:
    h = (h + 23) % 24
m = (m + 15) % 60
print(h, m)