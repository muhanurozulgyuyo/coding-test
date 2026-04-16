def solution(n):
    answer = []
    count = 2
    while n > 1:
        if n % count == 0:
            answer.append(count)
            while n % count == 0:
                n = n // count
        count += 1
            
    return answer