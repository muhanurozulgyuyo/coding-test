#1193 분수찾기

import sys

X = int(input())

# 대각선의 번호(diagonal number)를 구하기
diagonal = 1
while X > diagonal:
    X -= diagonal
    diagonal += 1

# 대각선이 짝수번째인 경우
if diagonal % 2 == 0:
    numerator = X
    denominator = diagonal - X + 1
# 대각선이 홀수번째인 경우
else:
    numerator = diagonal - X + 1
    denominator = X

print(f"{numerator}/{denominator}")
