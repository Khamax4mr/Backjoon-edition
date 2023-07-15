# 숫자 개수 n 입력.
n = int(input())
assert 0 <= n <= 100

# 숫자 numbers 입력.
numbers = list(map(int, input().split()))
assert not False in [0 <= number <= 1000 for number in numbers]

prime_count = 0
for number in numbers:
    # 정의에 따라 소수가 아닌 1 생략.
    if number == 1: continue

    is_dividable = (number % divisor == 0 for divisor in range(2, int(number**0.5)+1))
    prime_count += True not in is_dividable

print(prime_count)