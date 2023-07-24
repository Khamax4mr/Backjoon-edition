# 숫자 a, b의 최대공약수를 구하는 함수.
# return 최대공약수
def gcd(a, b):
    # a를 큰 숫자로 가정.
    a, b = max(a, b), min(a, b)
    while (a % b) and (b > 1):
        a = a % b
        a, b = max(a, b), min(a, b)
    return b

# 분자 a1, 분모 b1 입력.
a1, b1 = map(int, input().split())
assert 0 < a1 <= 30000
assert 0 < b1 <= 30000

# 분자 a2, 분모 b2 입력.
a2, b2 = map(int, input().split())
assert 0 < a2 <= 30000
assert 0 < b2 <= 30000

a_result = a1*b2 + a2*b1
b_result = b1*b2
b_gcd = gcd(a_result, b_result)
print(int(a_result/b_gcd), int(b_result/b_gcd))