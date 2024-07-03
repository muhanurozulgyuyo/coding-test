def solution(numbers, k):
    n = len(numbers)
    current_index = 0  # 시작 인덱스
    
    for _ in range(k - 1):  # 첫 번째 던짐은 현재 위치에서 시작이므로 k-1 번만 이동
        current_index = (current_index + 2) % n  # 두 명을 건너뛰고 다음 사람

    return numbers[current_index]

