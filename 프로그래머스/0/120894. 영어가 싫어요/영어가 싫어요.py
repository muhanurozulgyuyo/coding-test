def solution(numbers):
    answer = []
    nums = {
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9',
        'zero':'0'
    }
    count = 0
    for i in range(1, len(numbers)+1):
        if numbers[count:i] in nums.keys():
            answer.append(nums[numbers[count:i]])
            count = i
    return int(''.join(answer))