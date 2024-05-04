import sys

N, M = map(int, sys.stdin.readline().split())

A = []
B = []

# 행렬 A 입력 받기
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    A.append(row)
    
# 행렬 B 입력 받기
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    B.append(row)
    
# 행렬의 합 계산
result = []
for i in range(N):
    temp = []
    for j in range(M):
        temp.append(A[i][j] + B[i][j])
    result.append(temp)
        
# 결과 출력
for row in result:
    print(*row)
