def FindTriangle():
    li = []

    for i in range(3):
        angle = int(input())
        li.append(angle)

    set_li = list(set(li))

    if (sum(li) != 180) or (0 in set_li):
        print('Error')
    
    elif len(set_li) == 1:
        print('Equilateral')

    elif len(set_li) == 2:
        print('Isosceles')

    else:
        print('Scalene')

FindTriangle()