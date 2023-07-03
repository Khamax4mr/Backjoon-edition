from sys import exit

# 학생 수 n, 수상자 수 k 입력.
n, k = map(int, input().split())
if not 1 <= n <= 1000: exit()
if not 1 <= k <= n: exit()

# 점수 scores 입력.
scores = list(map(int, input().split()))
if True in [not 0 <= score <= 10000 for score in scores]: exit()

scores.sort(reverse=True)
print(scores[k-1])