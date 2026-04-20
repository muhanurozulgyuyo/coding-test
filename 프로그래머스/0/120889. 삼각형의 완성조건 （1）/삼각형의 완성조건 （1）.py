def solution(sides):
    answer = 0
    li = sorted(sides)
    if li[0] + li[1] > li[2]:
        return 1
    else:
        return 2