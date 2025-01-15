def solution(arr, intervals):
    answer = []
    for i in arr[intervals[0][0] : intervals[0][1] + 1]:
        answer.append(i)
    for i in arr[intervals[1][0] : intervals[1][1] + 1]:
        answer.append(i)
    return answer