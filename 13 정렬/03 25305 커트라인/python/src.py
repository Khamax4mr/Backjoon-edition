from sys import exit

# 학생 수 n, 수상자 수 k 입력.
n, k = map(int, input().split())
if n < 1 or n > 1000: exit(0)
if k < 1 or k > n: exit(0)

# 점수 scores 입력.
scores = list(map(int, input().split()))
if True in [score < 0 or score > 10000 for score in scores]: exit(0)

scores.sort(reverse=True)
print(scores[k-1])