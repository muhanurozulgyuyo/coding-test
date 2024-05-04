import sys

# 입력 받기
N = int(sys.stdin.readline())
paper = [[0] * 100 for _ in range(100)]  # 도화지 생성

# 색종이 덮기
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

# 면적 계산
area = 0
for i in range(100):
    area += sum(paper[i])

# 결과 출력
print(area)
