import sys
readlines = sys.stdin.readlines

# 단어 개수 n 입력.
n = int(input())
assert 1 <= n <= 20000

words = [word.rstrip('\n') for word in list(set(readlines()))]
assert not False in [1 <= len(word) <= 50 for word in words]

words.sort()
words.sort(key=len)
print('\n'.join(words))