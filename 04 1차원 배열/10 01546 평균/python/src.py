from sys import exit

# 과목 개수 n 입력.
n = int(input())
if not 0 <= n <= 1000: exit()

# 점수 scores 입력.
scores = list(map(int, input().split()))
if True in [not 0 <= score <= 100 for score in scores]: exit()

# 최대 점수 m 기준 점수 조작.
m = max(scores)
if m == 0: exit()
scores = [score / m * 100 for score in scores]
print(sum(scores) / len(scores))