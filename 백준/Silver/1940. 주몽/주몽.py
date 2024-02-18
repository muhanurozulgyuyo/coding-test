import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

start_idx = 0
end_idx = N - 1
count = 0

A.sort()

while start_idx < end_idx:
    if A[start_idx] + A[end_idx] < M:
        start_idx += 1
    elif A[start_idx] + A[end_idx] > M:
        end_idx -= 1
    else:
        count += 1
        start_idx += 1
        end_idx -= 1
        
print(count)