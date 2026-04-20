def solution(array, n):
    answer = array[0]
    
    for i in range(len(array)):
        if abs(array[i] - n) < abs(answer - n):
            answer = array[i]
        elif abs(array[i] - n) == abs(answer - n):
            if array[i] < answer:
                answer = array[i]
                
    return answer