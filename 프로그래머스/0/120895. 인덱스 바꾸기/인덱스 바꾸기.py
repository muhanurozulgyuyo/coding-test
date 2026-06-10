def solution(my_string, num1, num2):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[i])
    tmp1 = answer[num1]
    tmp2 = answer[num2]
    answer[num1] = tmp2
    answer[num2] = tmp1
    return ''.join(answer)