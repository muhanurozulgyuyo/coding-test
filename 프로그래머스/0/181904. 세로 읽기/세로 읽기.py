def solution(my_string, m, c):
    # 문자열을 m 단위로 나눔
    chunks = [my_string[i:i + m] for i in range(0, len(my_string), m)]
    # 각 청크의 c번째 문자 추출
    result = ''.join(chunk[c - 1] for chunk in chunks if len(chunk) >= c)
    return result
