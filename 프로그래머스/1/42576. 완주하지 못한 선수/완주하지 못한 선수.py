def solution(participant, completion):
    # 해시 테이블 생성
    p_dict = {}
    
    # 참가자 명단을 해시 테이블에 기록
    for person in participant:
        if person in p_dict:
            p_dict[person] += 1
        else:
            p_dict[person] = 1
    
    # 완주자 명단을 해시 테이블에서 차감
    for person in completion:
        if person in p_dict:
            p_dict[person] -= 1
    
    # 해시 테이블에서 값이 1인 선수가 완주하지 못한 선수
    for person in p_dict:
        if p_dict[person] == 1:
            return person
