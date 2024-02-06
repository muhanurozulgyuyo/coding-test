N = [int(input()) for _ in range(10)]
E = set()

for n in N:
  E.add(n % 42)

print(len(E))
