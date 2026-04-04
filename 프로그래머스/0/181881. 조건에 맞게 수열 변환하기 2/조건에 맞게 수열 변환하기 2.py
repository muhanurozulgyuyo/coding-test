def solution(arr):
    answer = 0
    def tasks(arr):
        for i in range(len(arr)):
            if (arr[i] >= 50) & (arr[i] % 2 == 0):
                arr[i] = arr[i] / 2
            elif (arr[i] < 50) & (arr[i] % 2 != 0):                 arr[i] = (arr[i] * 2) + 1
        return arr
    new_arr = tasks(arr.copy())
    while arr != new_arr:
        arr = new_arr.copy()
        new_arr = tasks(new_arr.copy())
        answer += 1
    return answer