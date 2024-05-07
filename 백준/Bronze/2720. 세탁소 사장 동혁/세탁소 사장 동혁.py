#2720 세탁소 사장 동혁

import sys

T = int(sys.stdin.readline())

Quater = 25
Dime = 10
Nickel = 5
Penny = 1

li = []

for i in range(T):
    Q_c = 0
    D_c = 0
    N_c = 0
    P_c = 0
    
    C = int(sys.stdin.readline())
    
    while C != 0:
        if C >= Quater:
            Q_c += 1
            C -= Quater
        elif C >= Dime:
            D_c += 1
            C -= Dime
        elif C >= Nickel:
            N_c += 1
            C -= Nickel
        elif C >= Penny:
            P_c += 1
            C -= Penny
    
    li.append([Q_c, D_c, N_c, P_c])
    
for i in range(len(li)):
    print(*li[i])