def find(li):
    cnt = 0
    for i in range(n):
        tmp = 0
        for j in range(n):
            if li[i][j] == 'X':
                if tmp >= 2:
                    cnt += 1
                tmp = 0
            else:
                tmp += 1
        if tmp >=2: #마지막 원소까지 지나왔다면
            cnt += 1
    return cnt
n = int(input())
r1 = [list(input()) for _ in range(n)]
r2 = [[r1[i][j] for i in range(n)] for j in range(n)]
print(find(r1),find(r2))