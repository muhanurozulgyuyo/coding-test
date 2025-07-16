def DefineTriangle():
    while True:
        x, y, z = map(int, input().split())
        li = [x, y, z]

        if sum(li) == 0:
            break

        li.sort()
        set_li = list(set(li))

        if li[2] >= li[0] + li[1]:
            print('Invalid')

        elif len(set_li) == 1:
            print('Equilateral')

        elif len(set_li) == 3:
            print('Scalene')

        else:
            print('Isosceles')

DefineTriangle()