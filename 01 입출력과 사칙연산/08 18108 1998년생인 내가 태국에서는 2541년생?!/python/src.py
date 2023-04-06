from sys import exit

# 연도 year 입력.
year = int(input())
if year < 1000 or year > 3000: exit()

print(year - 543)