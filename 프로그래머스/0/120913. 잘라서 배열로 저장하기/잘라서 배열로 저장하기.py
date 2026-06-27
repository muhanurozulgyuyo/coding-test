def solution(my_str, n):
    answer = []
    cnt = 0
    six = 0
    for i in range(len(my_str)):
        cnt += 1
        if cnt % n == 0:
            answer.append(my_str[six:cnt])
            six += n
        elif len(my_str[six:]) < n:
            answer.append(my_str[six:])
            break
    return answer