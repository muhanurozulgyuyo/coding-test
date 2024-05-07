#2745 진법 변환

import sys

N, B = map(str, sys.stdin.readline().split())
B = int(B)

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alp_val = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}
sum = 0

for i, alp in zip(range(len(alphabet)), alphabet):
    alp_val[alp] = i + 10
    
for s, i in zip(N, range(len(N))):
    sum += alp_val[s] * (B ** (len(N) - 1 - i))
    
print(sum)