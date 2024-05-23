import sys

N, K = map(int, sys.stdin.readline().split())
li = []

for n in range(1, N + 1):
    if N % n == 0:
        li.append(n)

if len(li) < K:
    print(0)
else:
    print(li[K - 1])