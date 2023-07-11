from sys import exit
from string import ascii_uppercase

# 단어 word 입력.
word = input()
if not 0 <= len(word) <= 1000000: exit()
if not word.isalpha(): exit()
word = word.upper()

# 알파벳 개수 구성.
alphabet_count = [word.count(alphabet) for alphabet in ascii_uppercase]
alphabet_max_count = max(alphabet_count)
if alphabet_count.count(alphabet_max_count) > 1:
    print('?')
else:
    print(ascii_uppercase[alphabet_count.index(alphabet_max_count)])