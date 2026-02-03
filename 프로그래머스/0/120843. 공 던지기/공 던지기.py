def solution(numbers, k):
    answer = 0
    if len(numbers) < k * 2:
        numbers = numbers * k
    return numbers[::2][k - 1]
