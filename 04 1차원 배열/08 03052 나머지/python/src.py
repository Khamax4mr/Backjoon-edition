from sys import exit, stdin

# 숫자 n 입력.
n = [int(line.strip()) for line in stdin.readlines()]
if True in [not 0 <= number <= 1000 for number in n]: exit()

remainer = [number % 42 for number in n]
print(len(set(remainer)))