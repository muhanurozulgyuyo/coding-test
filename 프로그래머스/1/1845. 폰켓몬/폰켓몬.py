def solution(nums):
    answer = 0
    
    num_set = set(nums)
    
    len_num = len(nums) // 2
    
    answer = min(len(num_set), len_num)
    
    return answer

