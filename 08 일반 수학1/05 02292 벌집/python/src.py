# 방 번호 n 입력.
n = int(input())
assert 1 <= n <= 1000000000

distance, max_room_id = 1, 1
while n > max_room_id:
    max_room_id += distance*6
    distance += 1

print(distance)