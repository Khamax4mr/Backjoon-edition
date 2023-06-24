from sys import exit

# 단어 word 입력.
word = input()
if not 2 <= len(word) <= 15: exit()

# 다이얼 번호 배치.
alphabet_numbers = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9]
alphabet_costs = [number + 1 for number in alphabet_numbers]
time_costs = [alphabet_costs[ord(word[i]) - ord('A')] for i in range(len(word))]
print(sum(time_costs))