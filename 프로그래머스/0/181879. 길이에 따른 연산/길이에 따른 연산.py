def solution(num_list):
    answer = 1
    if len(num_list) >= 11:
        answer = 0
        for i in range(len(num_list)):
            answer += num_list[i]
    else:
        for i in range(len(num_list)):
            answer = answer * num_list[i]        
    return answer