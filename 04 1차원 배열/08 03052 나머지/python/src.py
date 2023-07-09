from sys import exit

# 숫자 입력.
remainer = set()
for number in [int(input()) for _ in range(10)]:
    if not 0 <= number <= 1000: exit()
    remainer.add(number % 42)

print(len(remainer))