from sys import exit, stdin

# 집합 문자열 개수 n, 검사 문자열 개수 m 입력.
n, m = map(int, input().split())
if not 1 <= n <= 10000: exit()
if not 1 <= m <= 10000: exit()

# 집합 문자열 s 입력.
s = set(stdin.readline().rstrip() for _ in range(n))
if True in [len(word) > 500 for word in s]: exit()

# 검사 문자열 words 입력.
words = [stdin.readline().rstrip() for _ in range(m)]
if True in [len(word) > 500 for word in words]: exit()

print(sum([words.count(word) for word in s]))