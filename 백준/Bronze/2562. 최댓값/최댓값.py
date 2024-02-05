# 입력 받기
nums = []
for _ in range(9):
    nums.append(int(input()))

# 최댓값 찾기
max_num = max(nums)

# 최댓값의 순서 찾기
max_idx = nums.index(max_num) + 1

# 결과 출력
print(max_num)
print(max_idx)
