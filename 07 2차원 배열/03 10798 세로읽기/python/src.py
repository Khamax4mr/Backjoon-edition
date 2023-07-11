from sys import exit

vertical_dummy_word = ['*'] * 15 * 5
for i in range(5):
    # 단어 word 입력.
    word = input()
    if not 1 <= len(word) <= 15: exit()
    if not word.isalnum(): exit()

    for j in range(len(word)):
        vertical_dummy_word[j*5 + i] = word[j]

# 불필요한 더미 기호 제거.
print(''.join(map(str, vertical_dummy_word)).replace('*', ''))