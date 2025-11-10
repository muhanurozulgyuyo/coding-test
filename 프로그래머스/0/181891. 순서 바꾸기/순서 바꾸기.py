def solution(num_list, n):
    head = num_list[n:]
    tail = num_list[:n]
    answer = head+tail
    return answer