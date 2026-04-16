def solution(s):
    answer = 0
    li = []
    li = s.split(' ')
    for i in range(len(li)):
        if li[i] == 'Z':
            answer -= int(li[i - 1])
        else:
            answer += int(li[i])
    return answer