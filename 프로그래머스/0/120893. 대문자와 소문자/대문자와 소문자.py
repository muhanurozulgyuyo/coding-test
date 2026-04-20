def solution(my_string):
    answer = ''
    for i in range(len(my_string)):
        if my_string[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            answer = answer + my_string[i].lower()
        else:
            answer = answer + my_string[i].upper()
    return answer