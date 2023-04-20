from sys import exit

# 숫자 n 입력.
n = [int(input()) for i in range(10)]
if True in [number < 0 or number > 1000 for number in n]: exit(0)

# 나머지 구성.
remainer = [number % 42 for number in n]
print(len(set(remainer)))