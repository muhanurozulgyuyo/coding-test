N = int(input())
cnt = 1
num = 1

while num < N:
    num += 6 * cnt  # 각 층의 벌집 수
    cnt += 1  # 다음 층으로 이동

print(cnt)
