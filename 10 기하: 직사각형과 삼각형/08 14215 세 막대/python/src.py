from sys import exit

# 숫자 a, b, c를 오름차순으로 정렬하는 함수.
# return 정렬된 a, b, c 리스트.
def sort_triangle(a, b, c):
    sorted_list = [a, b, c]
    sorted_list.sort()
    return sorted_list

# 세 변의 길이 a, b, c 입력.
a, b, c = map(int, input().split())
if not 1 <= a <= 1000: exit()
if not 1 <= b <= 1000: exit()
if not 1 <= c <= 1000: exit()

# 각 변을 오름차순 정렬하여 c가 제일 큰 수임을 가정.
a, b, c = sort_triangle(a, b, c)
if a + b <= c:
    print(min(a + b, c)*2 - 1)
else:
    print(a + b + c)