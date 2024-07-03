def solution(num_list, n):
    s = len(num_list) // n
    answer = []
    
    for i in range(s):
        li = []
        for j in range(n):
            a = num_list.pop(0)
            li.append(a)
        answer.append(li)
    
    return answer