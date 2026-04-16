def solution(my_string):
    answer = ''
    for i in range(len(my_string)):
        tmp = my_string[i]
        if tmp not in 'aeiou':
            answer = answer + tmp
        elif tmp == ' ':
            answer = answer + ' '
    return answer