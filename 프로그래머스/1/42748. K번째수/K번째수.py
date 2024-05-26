def solution(array, commands):
    result = []
    for command in commands:
        i, j, k = command
        sub_array = sorted(array[i-1:j])
        result.append(sub_array[k-1])
    return result