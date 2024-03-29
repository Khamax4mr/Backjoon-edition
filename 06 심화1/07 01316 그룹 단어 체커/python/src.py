# 단어 개수 n 입력.
n = int(input())
assert 0 <= n <= 100

group_words = n
for _ in range(n):
    # 단어 word 입력.
    word = input()
    assert len(word) <= 100
    assert word.islower()

    # 알파벳 사용 내역 확인.
    used_alphabets = ['*']
    for i in range(len(word)):
        if used_alphabets[-1] == word[i]: continue
        elif word[i] not in used_alphabets:
            used_alphabets.append(word[i])
        else:
            group_words -= 1
            break

print(group_words)