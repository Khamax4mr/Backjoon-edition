from sys import exit

# 연도 year 입력.
year = int(input())
if not 1 <= year <= 4000: exit()

if year % 400 == 0: print(1)
elif year % 100 == 0: print(0)
elif year % 4 == 0: print(1)
else: print(0)