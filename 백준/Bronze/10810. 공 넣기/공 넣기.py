def solution(n, m, operations):
  """
  도현이 바구니 문제를 해결하는 함수입니다.

  Args:
    n: 바구니의 총 개수 (1 ≤ n ≤ 100)
    m: 공을 넣는 횟수 (1 ≤ m ≤ 100)
    operations: 공을 넣는 방법을 나타내는 리스트 (각 요소는 [i, j, k] 형태)

  Returns:
    각 바구니에 들어있는 공의 번호 리스트 (공이 없으면 0)
  """

  # 1번부터 n번까지 번호가 적힌 공을 담을 바구니 리스트 생성
  baskets = [0] * n

  for i, j, k in operations:
    # i번째부터 j번째까지 k번 공을 넣음
    for basket_idx in range(i - 1, j):
      baskets[basket_idx] = k

  return baskets

# 입력 받기
n, m = map(int, input().split())
operations = [list(map(int, input().split())) for _ in range(m)]

# 결과 출력
baskets = solution(n, m, operations)
print(*baskets)

# 예시 입력
# 5 4
# 1 2 3
# 3 4 4
# 1 4 1
# 2 2 2

# 예시 출력
# 3 4 1 0 0
