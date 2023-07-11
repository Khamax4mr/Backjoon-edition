from sys import exit

# 보드 세로 크기 m, 가로 크기 n 입력.
m, n = map(int, input().split())
if not 8 <= m <= 50: exit()
if not 8 <= n <= 50: exit()

wb_mask = 'WB'*(n//2) + 'W'*(n%2)
wb_fix_counts = [[64 for _ in range(n-7)] for _ in range(m-7)]

for i in range(m):
    # 보드 한 줄의 색깔 line 입력.
    line = input()
    if not len(line) == n: exit()
    if False in [a in 'BW' for a in line]: exit()

    # WB로 시작하면 WB 마스크, BW로 시작하면 BW 마스크 적용.
    if i % 2 == 0:
        masked_line = [line[j] == wb_mask[j] for j in range(n)]
    else:
        masked_line = [line[j] != wb_mask[j] for j in range(n)]

    # WB로 시작하는 보드 기준 수정 횟수 기록.
    fixed_line = [masked_line[x:x+8].count(False) for x in range(n-7)]
    for y in range(max(i-7, 0), min(i+1, m-7)):
        wb_fix_counts[y] = [(wb_fix_count + fix) % 64 for wb_fix_count, fix in zip(wb_fix_counts[y], fixed_line)]

# WB 시작, BW 시작 기준 별 최소 수정 횟수 계산.
min_wb_fix = min([min(i) for i in wb_fix_counts])
min_bw_fix = min([64 - max(i) for i in wb_fix_counts])
print(min(min_wb_fix, min_bw_fix))