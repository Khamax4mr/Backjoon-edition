result_scores = []
total_score = 0
for _ in range(20):
    # 과목명 name, 학점 score, 등급 grade 입력.
    input_data = input().split()
    name, score, grade = input_data[0], float(input_data[1]), input_data[2]
    assert 1 <= len(name) <= 50
    assert score in (1.0, 2.0, 3.0, 4.0)
    assert grade in ('A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F', 'P')

    # 학점 × 과목 평점.
    if grade == 'P': continue
    elif grade == 'A+': result_scores.append(score * 4.5)
    elif grade == 'A0': result_scores.append(score * 4.0)
    elif grade == 'B+': result_scores.append(score * 3.5)
    elif grade == 'B0': result_scores.append(score * 3.0)
    elif grade == 'C+': result_scores.append(score * 2.5)
    elif grade == 'C0': result_scores.append(score * 2.0)
    elif grade == 'D+': result_scores.append(score * 1.5)
    elif grade == 'D0': result_scores.append(score * 1.0)
    elif grade == 'F': result_scores.append(0)

    # 학점의 총합.
    total_score += score

print(f"{(sum(result_scores) / total_score):.6f}")