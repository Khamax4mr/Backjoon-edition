from sys import exit

# 나머지 여부 구성.
remainer = [False] * 43
for i in range(10):
    # 숫자 n 입력.
    n = int(input())
    if n < 0 or n > 1000: exit(0)
    
    remainer[n % 42] = True

print(remainer.count(True))