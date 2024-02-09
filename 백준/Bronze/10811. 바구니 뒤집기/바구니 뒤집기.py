N, M = map(int, input().split())

li = []
for q in range(1, N + 1):
    li.append(q)

for p in range(M):
    i, j = map(int, input().split())
    li[i - 1:j] = li[i - 1:j][::-1]

print(*li)
