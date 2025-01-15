def solution(arr):
    li = []
    if arr.count(2) == 1:
        return [2]
    elif arr.count(2) == 0:
        return [-1]
    else:
        for i in range(len(arr)):
            if arr[i] == 2:
                li.append(i)
        return arr[li[0] : li[-1] + 1]