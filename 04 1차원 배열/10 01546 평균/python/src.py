# 과목 개수 n 입력.
n = int(input())
assert 0 <= n <= 1000

# 점수 scores 입력.
scores = list(map(int, input().split()))
assert not False in [0 <= score <= 100 for score in scores]

# 최대 점수 m 기준 점수 조작.
m = max(scores)
assert not m == 0
scores = [score / m * 100 for score in scores]
print(sum(scores) / len(scores))