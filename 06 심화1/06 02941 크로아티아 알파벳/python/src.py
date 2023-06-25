from sys import exit

# 단어 word 입력.
word = input()
if len(word) > 100: exit()

# 크로아티아 알파벳을 임의의 문자 *로 수정.
alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for alphabet in alphabets:
    word = word.replace(alphabet, '*')
print(len(word))