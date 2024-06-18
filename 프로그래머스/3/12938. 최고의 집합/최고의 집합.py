def solution(n, s):
    if n > s:
        return [-1]

    quotient = s // n
    remainder = s % n

    # quotient를 n - remainder 만큼, quotient + 1을 remainder 만큼 추가
    answer = [quotient] * (n - remainder) + [quotient + 1] * remainder

    return answer
