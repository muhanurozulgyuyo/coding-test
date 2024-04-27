#2444 별 찍기 - 7

N = int(input())

for i in range(1, (N * 2)):
    if i <= N:
        print(f"{' ' * (N - i)}{((2 * i) - 1) * '*'}")
    else:
        print(f"{' ' * (i - N)}{((2 * ((2 * N) - i)) - 1) * '*'}")