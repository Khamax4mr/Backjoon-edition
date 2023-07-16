# 학생 수 n, 수상자 수 k 입력.
n, k = map(int, input().split())
assert 1 <= n <= 1000
assert 1 <= k <= n

# 점수 scores 입력.
scores = list(map(int, input().split()))
assert not False in [not 0 <= score <= 10000 for score in scores]

scores.sort(reverse=True)
print(scores[k-1])