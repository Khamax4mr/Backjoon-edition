# 정수 개수 n, 기준 정수 x 입력.
n, x = map(int, input().split())
assert 1 <= n <= 10000
assert 1 <= x <= 10000

# 배열 입력.
numbers_under_x = []
for number in tuple(map(int, input().split())):
    assert 1 <= number <= 10000
    if number >= x: continue
    numbers_under_x.append(number)

print(' '.join(str(x) for x in numbers_under_x))