def solution(order):
    answer = 0
    for i in range(len(str(order))):
        if str(order)[i] in '369':
            answer += 1
    return answer