from sys import exit

# 점수 score 입력.
score = int(input())
if not 0 <= score <= 100: exit()

if score >= 90: print('A')
elif score >= 80: print('B')
elif score >= 70: print('C')
elif score >= 60: print('D')
else: print('F')