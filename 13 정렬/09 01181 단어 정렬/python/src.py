from sys import exit, stdin

# 단어 개수 n 입력.
n = int(input())
if not 1 <= n <= 20000: exit()

words = [word.rstrip('\n') for word in list(set(stdin.readlines()))]
if True in [not 1 <= len(word) <= 50 for word in words]: exit()

words.sort()
words.sort(key=len)
print('\n'.join(words))