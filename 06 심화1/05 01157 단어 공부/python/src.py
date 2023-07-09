from sys import exit

# 단어 word 입력.
word = input().upper()
if not 0 <= len(word) <= 1000000: exit()

# 알파벳 개수 구성.
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_count = [word.count(alphabet) for alphabet in alphabets]
alphabet_max_count = max(alphabet_count)
if alphabet_count.count(alphabet_max_count) > 1:
    print('?')
else:
    print(alphabets[alphabet_count.index(alphabet_max_count)])