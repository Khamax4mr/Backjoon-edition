# 숫자 입력.
remainer = set()
for number in tuple(int(input()) for _ in range(10)):
    assert 0 <= number <= 1000
    remainer.add(number % 42)

print(len(remainer))