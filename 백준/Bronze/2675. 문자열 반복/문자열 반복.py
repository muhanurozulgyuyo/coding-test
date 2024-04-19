# 테스트 케이스의 개수 입력 받기
t = int(input())

for _ in range(t):
    S = ''
    li = []
    R, P = map(str, input().split())
    r = int(R)
    p = [s for s in P]

    for i in p:
        li.append(i * r)

    for i in range(len(li)):
        S = S + li[i]
    print(S)