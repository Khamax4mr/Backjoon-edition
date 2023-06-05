from sys import exit

# 카드 개수 n, 딜러 선언 숫자 m 입력.
n, m = map(int, input().split())
if n < 3 or n > 100: exit(0)
if m < 10 or m > 300000: exit(0)

# 카드 번호 목록 cards 입력.
cards = list(map(int, input().split()))
if True in [id < 0 or id > 100000 for id in cards]: exit(0)

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