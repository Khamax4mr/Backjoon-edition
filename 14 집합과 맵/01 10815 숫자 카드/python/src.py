from sys import exit, stdin

# 보유 카드 개수 n 입력.
n = int(input())
if not 1 <= n <= 500000: exit()

# 보유 카드 숫자 hands 입력.
hands = set(map(int, stdin.readline().rstrip().split()))
if True in [not -10000000 <= number <= 10000000 for number in hands]: exit()

# 비교 카드 개수 m 입력.
m = int(input())
if not 1 <= n <= 500000: exit()

# 비교 카드 숫자 matches 입력.
matches = list(map(int, stdin.readline().rstrip().split()))
if True in [not -10000000 <= number <= 10000000 for number in matches]: exit()

print(' '.join(map(str, [1 if number in hands else 0 for number in matches])))