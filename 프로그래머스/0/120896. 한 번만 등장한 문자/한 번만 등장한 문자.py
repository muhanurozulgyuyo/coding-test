def solution(s):
    answer = []
    while len(s) > 0:
        if s[0] in s[1:]:
            s = s.replace(s[0], '')
        else:
            answer.append(s[0])
            s = s.replace(s[0], '')
    return ''.join(sorted(answer))
