#2566 최댓값

import sys

matrix = []

for _ in range(9):
    row = list(map(int, sys.stdin.readline().split()))
    matrix.append(row)

mx = []
    
for i in range(9):
    mx.append(max(matrix[i]))
    
max_idx_row = mx.index(max(mx))
max_idx_col = matrix[max_idx_row].index(max(matrix[max_idx_row]))

print(matrix[max_idx_row][max_idx_col])
print(max_idx_row + 1, max_idx_col + 1)