from sys import exit

# 연도 year 입력.
year = int(input())
if year < 1 or year > 4000: exit()

# 출력.
if year % 400 == 0: print(1)
elif year % 100 == 0: print(0)
elif year % 4 == 0: print(1)
else: print(0)