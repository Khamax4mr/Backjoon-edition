from sys import exit

while True:
    # 숫자 n 입력.
    n = int(input())
    if n == -1: break
    if n <= 2 or n >= 100000: exit(0)

    # 약수 구하기.
    divisors = []
    for divisor in range(1, n):
        if n % divisor == 0: divisors.append(divisor)
    
    if n == sum(divisors):
        print(f"{n} = {' + '.join(map(str, divisors))}")
    else:
        print(f"{n} is NOT perfect.")