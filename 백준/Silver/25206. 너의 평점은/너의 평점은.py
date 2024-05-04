import sys

N = 20

GPA = {'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5, 'B0' : 3.0, 'C+' : 2.5, 'C0' : 2.0, 'D+' : 1.5, 'D0' : 1.0, 'F' : 0.0}

fin_credit = 0
sum_credit = 0

for i in range(N):
    S, C, G = map(str, sys.stdin.readline().split())
    C = float(C)
    
    if G != 'P':
        fin_credit += C * GPA[G]
        sum_credit += C

if sum_credit != 0:
    print(fin_credit / sum_credit)
else:
    print("No credit earned.")
