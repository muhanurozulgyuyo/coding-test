#5622 다이얼

S = input()
T = 0

for s in S:
    if s in 'ABC':
        T += 3
    elif s in 'DEF':
        T += 4
    elif s in 'GHI':
        T += 5
    elif s in 'JKL':
        T +=6
    elif s in 'MNO':
        T += 7
    elif s in 'PQRS':
        T += 8
    elif s in 'TUV':
        T += 9
    else:
        T += 10

print(T)