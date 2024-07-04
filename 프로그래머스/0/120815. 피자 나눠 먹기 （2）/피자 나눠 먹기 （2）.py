def solution(n):
    # 최소 공배수를 구하는 함수
    def lcm(x, y):
        greater = max(x, y)
        while True:
            if greater % x == 0 and greater % y == 0:
                return greater
            greater += 1
    
    # 6과 n의 최소 공배수를 구합니다.
    least_common_multiple = lcm(6, n)
    
    # 필요한 피자 판 수는 최소 공배수를 6으로 나눈 값입니다.
    pizzas_needed = least_common_multiple // 6
    
    return pizzas_needed