S = input()

cro_S = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

cnt = 0

# 문자열을 한 번만 순회하여 크로아티아 알파벳을 찾고 대체합니다.
for s in cro_S:
    if s in S:
        cnt += S.count(s)  # 해당 크로아티아 알파벳의 개수를 카운트에 추가
        S = S.replace(s, ' ', S.count(s))  # 해당 크로아티아 알파벳을 모두 공백으로 대체

S = S.replace(' ', '')  # 남은 문자열에서 공백 제거

print(cnt + len(S))  # 카운트와 남은 문자열의 길이를 합하여 출력
