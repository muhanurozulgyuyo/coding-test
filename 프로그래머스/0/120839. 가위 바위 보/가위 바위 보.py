def solution(rsp):
    answer = ''  # 문자열로 시작
    for i in range(len(rsp)):
        if rsp[i] == '2':
            answer += '0'    # += 를 사용하여 문자를 이어 붙임
        elif rsp[i] == '0':
            answer += '5'
        else:
            answer += '2'
    return answer