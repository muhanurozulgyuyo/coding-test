X = int(input())
N = int(input())

m = 0

for i in range(N):
    a, b = map(int, input().split())
    m += a * b
    
if m == X:
    print("Yes")
else:
    print("No")