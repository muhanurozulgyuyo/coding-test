def solution(num_list, n):
    li = []
    tmp = []

    for i in range(len(num_list)):
        tmp.append(num_list[i])
        if len(tmp) == n:
            li.append(tmp)
            tmp = []

    return li