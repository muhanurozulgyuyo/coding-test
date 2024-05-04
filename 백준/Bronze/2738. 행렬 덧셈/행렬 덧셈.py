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
for i in range(len(A)):
    temp = []
    for j in range(len(A[i])):
        temp.append(A[i][j] + B[i][j])
    result.append(temp)
        
for i in range(len(result)):
    print(*result[i])
