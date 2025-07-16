a, b, c = map(int, input().split())

li = [a, b, c]

li.sort()

if li[2] < li[0] + li[1]:
    print(sum(li))
else:
    li[2] = li[0] + li[1] - 1
    print(sum(li))