from sys import exit

# 설탕 용량 n 입력.
n = int(input())
if n < 3 or n > 5000: exit(0)

bag_5kg = n // 5
remained_n = n % 5

for _ in range(min(3, bag_5kg)):
    if remained_n % 3 == 0: break
    bag_5kg -= 1
    remained_n += 5
bag_3kg = remained_n // 3

print(-1 if remained_n % 3 else bag_5kg + bag_3kg)