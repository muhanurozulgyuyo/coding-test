import sys

s = [int(sys.stdin.readline().rstrip()) for i in range(28)]
n = [i for i in range(1, 31)]

for i in range(len(s)):
    if s[i] in n :
        n.remove(s[i])

print(min(n))
print(max(n))