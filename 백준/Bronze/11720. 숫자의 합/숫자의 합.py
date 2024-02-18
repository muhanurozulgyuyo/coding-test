def solve():
    # N과 문자열 입력
    n = int(input())
    s = input()

    # 문자열을 숫자 리스트로 변환
    numbers = list(map(int, s))

    # 숫자 합산
    total = sum(numbers)

    # 합산 결과 출력
    print(total)


# 풀이 실행
solve()