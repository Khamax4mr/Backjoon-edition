from sys import exit

# 나머지 유무 초기화.
remainer = [False] * 42

for i in range(10):
    # 숫자 n 입력.
    n = int(input())
    if n < 0 or n > 1000: exit(0)

    # 나머지 유무 적용.
    remainer[n % 42] = True

# 출력.
print(remainer.count(True))
