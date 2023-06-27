from sys import exit

# 숫자 n 입력.
n = [int(input()) for _ in range(10)]
if True in [not 0 <= number <= 1000 for number in n]: exit()

remainer = [number % 42 for number in n]
print(len(set(remainer)))