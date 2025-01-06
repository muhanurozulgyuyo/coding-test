def solution(my_string, is_prefix):
    li = []
    for i in range(len(my_string)):
        li.append(my_string[:i])
    if is_prefix in li:
        return 1
    else:
        return 0