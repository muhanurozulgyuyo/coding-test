def solution(numbers, direction):
    answer = []
    if direction == 'right':
        pop = numbers.pop()
        numbers.insert(0, pop)
        answer = numbers
    else:
        pop = numbers.pop(0)
        numbers.append(pop)
        answer = numbers
    return answer