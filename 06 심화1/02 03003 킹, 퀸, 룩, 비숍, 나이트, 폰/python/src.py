from sys import exit

# 체스 말 개수 king, queen, rook, bishop, knight, pawn 입력.
king, queen, rook, bishop, knight, pawn = map(int, input().split())
if not 0 <= king <= 10: exit()
if not 0 <= queen <= 10: exit()
if not 0 <= rook <= 10: exit()
if not 0 <= bishop <= 10: exit()
if not 0 <= knight <= 10: exit()
if not 0 <= pawn <= 10: exit()

print(1-king, 1-queen, 2-rook, 2-bishop, 2-knight, 8-pawn)