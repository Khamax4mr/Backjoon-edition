from sys import exit

# 연도 year 입력.
year = int(input())
if not 1000 <= year <= 3000: exit()

print(year - 543)