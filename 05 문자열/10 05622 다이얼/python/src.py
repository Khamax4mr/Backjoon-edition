# 단어 word 입력.
word = input()
assert 2 <= len(word) <= 15
assert word.isupper()

# 다이얼 번호 배치.
alphabet_costs = tuple(3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10)
time_costs = tuple(alphabet_costs[ord(word[i]) - ord('A')] for i in range(len(word)))
print(sum(time_costs))