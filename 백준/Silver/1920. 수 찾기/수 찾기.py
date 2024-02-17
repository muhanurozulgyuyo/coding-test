import sys

N = int(sys.stdin.readline())

nums_set = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

nums = list(map(lambda x: 1 if x in nums_set else 0, nums))

print(*nums)
