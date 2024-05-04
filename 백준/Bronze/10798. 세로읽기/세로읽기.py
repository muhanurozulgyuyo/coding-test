import sys

matrix = []
li = []

for _ in range(5):
    row = list(map(str, sys.stdin.readline().split()))
    matrix.append(row)

for i in range(len(matrix)):
    for j in matrix[i]:
        row = []
        for s in j:
            row.append(s)
    matrix[i] = row

    li.append(len(matrix[i]))

for i in range(len(matrix)):
    while len(matrix[i]) < max(li):
        matrix[i].append(' ')

s = ''

for i in range(max(li)):
    for j in range(len(matrix)):
        s = s + matrix[j][i]
    
print(s.replace(' ', ''))