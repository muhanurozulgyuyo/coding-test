a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

# 모든 n ≥ n0에서 f(n) ≤ c × n 이어야 함
# 즉, a1 * n + a0 ≤ c * n

ok = True
for n in range(n0, 101):
    if a1 * n + a0 > c * n:
        ok = False
        break

print(1 if ok else 0)
