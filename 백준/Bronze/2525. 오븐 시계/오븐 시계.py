A,B = map(int, input().split())
C = int(input())

if (B + C) < 60:
  print(f"{A} {B+C}")
else:
  if ((B + C) // 60) + A < 24:
    print(f"{((B + C) // 60) + A} {(B + C) % 60}")
  else:
    print(f"{((B + C) // 60) + A - 24} {(B + C) % 60}")