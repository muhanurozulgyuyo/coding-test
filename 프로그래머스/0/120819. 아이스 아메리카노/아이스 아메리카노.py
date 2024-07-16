def solution(money):
    answer = []
    cnt = money // 5500
    if (cnt) >= 0:
        return [cnt, money - (5500 * cnt)]
    else:
        return [cnt, money]