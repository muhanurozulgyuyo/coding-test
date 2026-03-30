def solution(n):
    i = 1
    f = 1  # 팩토리얼 결과 저장
    while f <= n:
        i += 1
        f *= i
    
    # f가 n을 초과해서 반복문이 끝났으므로, 직전 단계인 i - 1이 정답입니다.
    return i - 1