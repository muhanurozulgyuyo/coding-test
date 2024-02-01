H, M = map(int, input().split())

if M - 45 >= 0:
    print(f"{H} {M - 45}")
else:
    if H == 0:
        print(f"{23} {60 + M - 45}")
    else:
        print(f"{H - 1} {60 + M - 45}")