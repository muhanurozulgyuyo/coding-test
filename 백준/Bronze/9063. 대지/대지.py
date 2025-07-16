N = int(input())

def find_square(N):
    if N == 1:
        x, y = map(int, input().split())
        
        return 0

    else:
        li_x = []
        li_y = []

        for i in range(N):
            x, y = map(int, input().split())

            li_x.append(x)
            li_y.append(y)

        max_x = max(li_x)
        min_x = min(li_x)

        max_y = max(li_y)
        min_y = min(li_y)
        
        return (max_x - min_x) * (max_y - min_y)

print(find_square(N))