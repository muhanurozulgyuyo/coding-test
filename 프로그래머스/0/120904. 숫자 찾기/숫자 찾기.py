def solution(num, k):
    num = str(num)
    k = str(k)
    nm = []
    for i in range(len(num)):
        nm.append(num[i])
    if k in num:
        return int(nm.index(k)) + 1
    else:
        return -1
    return answer