from sys import exit

# 테스트케이스 c 입력.
c = int(input())

for tasetcase_id in range(c):
    # 학생 수 n, 점수 scores 입력.
    testcase = list(map(int, input().split()))
    n, scores = testcase[0], testcase[1:]
    if n < 1 or n > 1000: exit(0)
    if True in [score < 0 or score > 100 for score in scores]: exit(0)

    # 평균 점수 초과 여부 계산.
    average_score = sum(scores) / len(scores)
    is_over_average = [True if score > average_score else False for score in scores]
    over_average_ratio = is_over_average.count(True) / len(is_over_average)
    print(f"{(over_average_ratio * 100):.3f}%")