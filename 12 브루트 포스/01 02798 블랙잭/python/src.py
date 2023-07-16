# 카드 개수 n, 딜러 선언 숫자 m 입력.
n, m = map(int, input().split())
assert 3 <= n <= 100
assert 10 <= m <= 300000

# 카드 번호 목록 cards 입력.
cards = list(map(int, input().split()))
assert not False in [0 <= id <= 100000 for id in cards]

# 편의를 위해 카드 오름차순 정렬.
cards.sort()
max_score = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            score = cards[i] + cards[j] + cards[k]
            # m을 넘어가면 조기 종료.
            if score > m: break
            max_score = max(max_score, score)
print(max_score)