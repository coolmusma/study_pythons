kor = [70, 80, 90, 40, 50]
eng = [90, 80, 70, 70, 60]
sum1, sum2 = 0, 0

# 국어 점수 출력 및 합계 계산
print("국어 점수:", end=' ')
for score in kor:
    print(score, end=' ')
    sum1 = score + sum1
print('\\n국어 합계 :', sum1)

print("-" * 20) # 구분선

# 영어 점수 출력 및 합계 계산
print("영어 점수:", end=' ')
for score in eng:
    print(score, end=' ')
    sum2 = score + sum2
print('\\n영어 합계 :', sum2)
