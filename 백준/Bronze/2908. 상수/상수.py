A, B = map(int, input().split())

rev_A = int(str(A)[::-1])
rev_B = int(str(B)[::-1])

li = [rev_A, rev_B]

print(max(li))