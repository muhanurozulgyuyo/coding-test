N = int(input())

max1 = 0

li = list(map(int, input().split()))

v = int(input())

for i in li:
    count = 0
    for j in li:
        if j == v:
            count += 1
    if count >= max1:
        max1 = count

print(max1)