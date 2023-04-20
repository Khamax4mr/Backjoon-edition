from sys import exit

# 과목 개수 n 입력.
n = int(input())
if n < 0 or n > 1000: exit(0)

# 점수 scores 입력.
scores = list(map(int, input().split()))
if True in [score < 0 or score > 100 for score in scores]: exit(0)

# 최대 점수 m 기준 점수 조작.
m = max(scores)
if m == 0: exit(0)
scores = [score / m * 100 for score in scores]
print(sum(scores) / len(scores))