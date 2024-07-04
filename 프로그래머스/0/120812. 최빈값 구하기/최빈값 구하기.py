def solution(array):
    # 빈도 계산을 위한 딕셔너리
    frequency = {}
    
    # 배열의 각 요소에 대해 빈도 계산
    for num in array:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # 가장 높은 빈도를 찾습니다.
    max_count = 0
    most_frequent = []
    
    for key, value in frequency.items():
        if value > max_count:
            max_count = value
            most_frequent = [key]
        elif value == max_count:
            most_frequent.append(key)
    
    # 최빈값이 여러 개인 경우 -1을 반환합니다.
    if len(most_frequent) > 1:
        return -1
    
    # 그렇지 않으면 최빈값을 반환합니다.
    return most_frequent[0]