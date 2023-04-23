from sys import exit

# 단어 word 입력.
word = input().upper()
if len(word) < 0 or len(word) > 1000000: exit(0)

# 알파벳 개수 구성.
alphabets = [chr(i) for i in range(ord('A'), ord('Z')+1)]
alphabet_index = [word.count(alphabet) for alphabet in alphabets]
alphabet_max = max(alphabet_index)
if alphabet_index.count(alphabet_max) > 1:
    print('?')
else:
    print(alphabets[alphabet_index.index(alphabet_max)])