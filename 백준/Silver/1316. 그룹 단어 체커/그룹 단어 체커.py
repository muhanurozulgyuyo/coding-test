N = int(input())
count = N

for _ in range(N):
    s = input().strip()  # 문자열 입력 받기
    seen = set()  # 등장한 문자를 저장할 집합
    prev_char = None  # 이전 문자를 저장할 변수
    for char in s:
        if prev_char != char:  # 이전 문자와 다를 때
            if char in seen:  # 이미 나왔던 문자인 경우
                count -= 1  # 그룹 단어가 아니므로 카운트를 줄임
                break
            seen.add(char)
        prev_char = char

print(count)
