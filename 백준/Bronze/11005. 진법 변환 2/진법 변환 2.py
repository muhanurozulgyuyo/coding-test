#11005 진법 변환2

import sys

N, B = map(int, sys.stdin.readline().split())

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alp_val = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}

for i, alp in zip(range(len(alphabet)), alphabet):
    alp_val[alp] = i + 10

new = []    

while N != 0:
    for key in alp_val.keys():
        if alp_val[key] == N % B:
            new.append(key)
    N = N // B
    
print(*new[::-1], sep = '')