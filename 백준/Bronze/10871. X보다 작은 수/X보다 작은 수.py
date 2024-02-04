N, X = map(int, input().split())

A = list(map(int, input().split()))

li = []

for i in range(N):
    if A[i] < X:
        li.append(A[i])
        
print(*li)