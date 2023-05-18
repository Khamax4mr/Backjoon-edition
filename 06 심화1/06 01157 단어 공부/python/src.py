from sys import exit

# 단어 word 입력.
word = input().upper()
if len(word) < 0 or len(word) > 1000000: exit(0)

# 알파벳 개수 구성.
alphabets = [chr(i) for i in range(ord('A'), ord('Z')+1)]
alphabet_count = [word.count(alphabet) for alphabet in alphabets]
alphabet_max_count = max(alphabet_count)
if alphabet_count.count(alphabet_max_count) > 1:
    print('?')
else:
    print(alphabets[alphabet_count.index(alphabet_max_count)])