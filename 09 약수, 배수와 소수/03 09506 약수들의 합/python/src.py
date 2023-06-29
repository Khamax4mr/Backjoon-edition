from sys import exit

while True:
    # 숫자 n 입력.
    n = int(input())
    if n == -1: break
    if not 2 < n < 100000: exit()

    # 최소한의 반복으로 약수 판단 후 전체 약수 목록 구성.
    base_divisors = [divisor for divisor in range(2, int(n**0.5)+1) if n % divisor == 0]
    divisors = list(sorted(set([1] + base_divisors + [n//divisor for divisor in base_divisors])))
    if n == sum(divisors):
        print(f"{n} = {' + '.join(map(str, divisors))}")
    else:
        print(f"{n} is NOT perfect.")