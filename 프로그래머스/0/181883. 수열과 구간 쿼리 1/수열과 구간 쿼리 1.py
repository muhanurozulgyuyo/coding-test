def solution(arr, queries):
    answer = []
    for j in range(len(queries)):
        s = queries[j][0]
        e = queries[j][1]
        for i in range(len(arr)):
            if i >= s and i <= e:
                arr[i] += 1
                
    return arr