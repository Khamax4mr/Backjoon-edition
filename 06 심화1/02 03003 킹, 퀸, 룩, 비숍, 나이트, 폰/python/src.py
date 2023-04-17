from sys import exit

# 체스 말 개수 king, queen, rook, bishop, knight, pawn 입력.
king, queen, rook, bishop, knight, pawn = map(int, input().split())
if king < 0 or king > 10: exit(0)
if queen < 0 or queen > 10: exit(0)
if rook < 0 or rook > 10: exit(0)
if bishop < 0 or bishop > 10: exit(0)
if knight < 0 or knight > 10: exit(0)
if pawn < 0 or pawn > 10: exit(0)

print(1 - king, 1 - queen, 2 - rook, 2 - bishop, 2 - knight, 8 - pawn)