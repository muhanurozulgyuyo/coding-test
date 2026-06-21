def solution(quiz):
    answer = []
    for i in range(len(quiz)):
        quiz[i] = quiz[i].split(' ')
        ans = int(quiz[i][0])
        for j in range(len(quiz[i])):
            if quiz[i][j] == '+':
                ans += int(quiz[i][j+1])
            elif quiz[i][j] == '-':
                ans -= int(quiz[i][j+1])
            elif quiz[i][j] == '=':
                if int(quiz[i][j+1]) == ans:
                    answer.append('O')
                else:
                    answer.append('X')

    return answer