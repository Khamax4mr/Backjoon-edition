# 숫자 n 입력.
n = int(input())
assert 1 <= n <= 10000000

# 소인수분해가 불가능하 1은 생략.
if n == 1: pass

# 소인수분해 최소 단위 2, 3은 그대로 출력.
elif n < 4: print(n)

# 나머지 소인수 출력.
else:
    for divisor in range(2, round(n**0.5)+1):
        while n % divisor == 0:
            print(divisor)
            n /= divisor

    # 나머지 소인수 출력.
    if n > 1: print(int(n))