from sys import exit, stdin, stdout

# 단어 개수 n 입력.
n = int(stdin.readline())
if n < 1 or n > 20000: exit(0)

words = [word.rstrip('\n') for word in list(set(stdin.readlines()))]
if True in [len(word) < 1 or len(word) > 50 for word in words]: exit(0)

words.sort()
words.sort(key=len)
stdout.write('\n'.join(words))