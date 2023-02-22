from sys import exit

# 좌표 x, y 입력.
x = int(input())
y = int(input())

if x < -1000 or x == 0 or x > 1000: exit(0)
if y < -1000 or y == 0 or y > 1000: exit(0)

# 출력.
if x > 0 and y > 0: print(1)
elif x < 0 and y > 0: print(2)
elif x < 0 and y < 0: print(3)
else: print(4)