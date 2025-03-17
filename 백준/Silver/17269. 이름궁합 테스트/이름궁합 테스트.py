N, M = map(int, input().split())
A, B = map(str, input().split())

def stroke_count(s):
    if s == 'A':
        return 3
    elif s == 'B':
        return 2
    elif s == 'C':
        return 1
    elif s == 'D':
        return 2
    elif s == 'E':
        return 4
    elif s == 'F':
        return 3
    elif s == 'G':
        return 1
    elif s == 'H':
        return 3
    elif s == 'I':
        return 1
    elif s == 'J':
        return 1
    elif s == 'K':
        return 3
    elif s == 'L':
        return 1
    elif s == 'M':
        return 3
    elif s == 'N':
        return 2
    elif s == 'O':
        return 1
    elif s == 'P':
        return 2
    elif s == 'Q':
        return 2
    elif s == 'R':
        return 2
    elif s == 'S':
        return 1
    elif s == 'T':
        return 2
    elif s == 'U':
        return 1
    elif s == 'V':
        return 1
    elif s == 'W':
        return 1
    elif s == 'X':
        return 2
    elif s == 'Y':
        return 2
    elif s == 'Z':
        return 1

def name_match(len1, len2, name1, name2):
    name1_count = []
    name2_count = []
    name_count = []


    for s in name1:
        name1_count.append(stroke_count(s))
    for s in name2:
        name2_count.append(stroke_count(s))

    if len1 >= len2:
        for i in range(len1):
            name_count.append(name1_count[i])
            if i < (len2):
                name_count.append(name2_count[i])
    else:
        for i in range(len2):
            if i < (len1):
                name_count.append(name1_count[i])
            name_count.append(name2_count[i])

    while len(name_count) > 2:
        new_name_count = []
        for i in range(len(name_count) - 1):
            pre = i
            now = i + 1
            name_sum = name_count[pre] + name_count[now]
            if name_sum >= 10:
                name_sum = name_sum % 10
            new_name_count.append(name_sum)
        name_count = new_name_count

    return f"{name_count[0] * 10 + name_count[1]}%"

print(name_match(N, M, A, B))