def solution(names):
    answer = []
    cnt = 0
    for i in range(len(names)):
        if cnt == 0:
            answer.append(names[i])
        elif cnt % 5 == 0:
            answer.append(names[i])
        cnt += 1

    return answer