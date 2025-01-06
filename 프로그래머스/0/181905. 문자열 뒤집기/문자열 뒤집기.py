def solution(my_string, s, e):
    answer = []
    li = my_string[s:e+1]
    for i in range(len(li)):
        answer.append(li[-i-1])
    return my_string[:s] + ''.join(answer) + my_string[e+1:]