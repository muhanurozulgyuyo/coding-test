def solution(arr, idx):
    answer = 0
    arr = arr[idx:]
    if 1 in arr:
        return arr.index(1) + idx
    else:
        return -1