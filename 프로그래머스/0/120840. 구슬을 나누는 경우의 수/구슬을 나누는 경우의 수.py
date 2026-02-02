def solution(balls, share):
    answer = 0
    b = 1
    s = 1
    k = 1
    for i in range(1, balls + 1):
        b = b * i
    for i in range(1, share + 1):
        s = s * i
    for i in range(1, balls-share+1):
        k = k * i
    answer = b / (s * k)
    return answer