def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        if my_string[i] in '0123456789':
            answer.append(int(my_string[i]))
    return sorted(answer)