# 숫자 n 입력.
n = list(input())
assert 1 <= len(n) <= 10

n.sort(reverse=True)
print(''.join(map(str, n)))