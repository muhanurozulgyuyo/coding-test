import sys

N, M = map(int, sys.stdin.readline().split())

ball = []

for k in range(1, N + 1):
    ball.append(k)
    
for p in range(M):
    i, j = map(int, sys.stdin.readline().split())
    temp = ball[i - 1]
    ball[i - 1] = ball[j - 1]
    ball[j - 1] = temp
    
print(*ball)