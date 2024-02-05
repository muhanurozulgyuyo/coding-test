N, M = map(int, input().split())

A = [0] * N

for p in range(M):
    i, j, k = map(int, input().split())
    for q in range(i - 1, j):
        A[q] = k
        
print(*A)