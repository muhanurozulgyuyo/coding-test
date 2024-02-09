N = int(input())
M = list(map(int, input().split()))

mx = max(M)

for i in range(len(M)):
    M[i] = ((M[i] / mx) * 100)

print(sum(M) / len(M))