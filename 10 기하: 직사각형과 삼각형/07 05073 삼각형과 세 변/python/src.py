import sys
readlines = sys.stdin.readlines

# 숫자 a, b, c를 오름차순으로 정렬하는 함수.
# return 정렬된 a, b, c 리스트.
def sort_triangle(a, b, c):
    sorted_list = [a, b, c]
    sorted_list.sort()
    return sorted_list

for line in readlines():
    # 세 변의 길이 a, b, c 입력.
    a, b, c = map(int, line.rstrip().split())
    if a == 0 and b == 0 and c == 0: break
    assert 0 < a <= 1000
    assert 0 < b <= 1000
    assert 0 < c <= 1000

    # 각 변을 오름차순 정렬하여 c가 제일 큰 수임을 가정.
    a, b, c = sort_triangle(a, b, c)
    if a + b <= c:
        print('Invalid')
    else:
        match = (a == b) + (b == c) + (c == a)
        if match == 3:
            print('Equilateral')
        elif match == 1:
            print('Isosceles')
        else:
            print('Scalene')