from sys import exit

# 점수 score 입력.
score = int(input())
if score < 0 or score > 100: exit()

# 출력.
if score >= 90: print('A')
elif score >= 80: print('B')
elif score >= 70: print('C')
elif score >= 60: print('D')
else: print('F')