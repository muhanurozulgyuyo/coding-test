def solution(n, lost, reserve):
    # 각 학생이 체육복을 몇 개 가지고 있는지 저장하는 리스트
    students = [1] * n
    
    # 체육복을 도난당한 학생의 체육복 개수 감소
    for l in lost:
        students[l - 1] -= 1
    
    # 여벌 체육복을 가진 학생의 체육복 개수 증가
    for r in reserve:
        students[r - 1] += 1
    
    # 체육복을 빌려주는 과정
    for i in range(n):
        if students[i] == 0:  # 체육복이 없는 경우
            if i > 0 and students[i - 1] == 2:  # 앞번호 학생이 여벌 체육복이 있는 경우
                students[i] = 1
                students[i - 1] = 1
            elif i < n - 1 and students[i + 1] == 2:  # 뒷번호 학생이 여벌 체육복이 있는 경우
                students[i] = 1
                students[i + 1] = 1
    
    # 체육복을 입을 수 있는 학생 수 계산
    count = sum(s >= 1 for s in students)
    
    return count