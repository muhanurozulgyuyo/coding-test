def solution(slice, n):
    count = 1
    new_slice = slice
    
    while new_slice < n:
        count += 1
        new_slice += slice
        
    return count
