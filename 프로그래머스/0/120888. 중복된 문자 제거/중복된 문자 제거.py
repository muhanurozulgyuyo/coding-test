def solution(my_string):
    li = []
    for i in range(len(my_string)):
        if my_string[i] not in li:
            li.append(my_string[i])
    return ''.join(li)