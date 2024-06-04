def solution(n, lost, reserve):
    # 여벌 체육복을 가진 학생이 도난당한 경우를 먼저 처리합니다.
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)

    # 체육복을 빌려줄 수 있는 경우를 처리합니다.
    for r in sorted(reserve_set):
        if r - 1 in lost_set:
            lost_set.remove(r - 1)
        elif r + 1 in lost_set:
            lost_set.remove(r + 1)

    # 체육복을 잃어버린 학생들을 제외한 학생 수를 반환합니다.
    return n - len(lost_set)