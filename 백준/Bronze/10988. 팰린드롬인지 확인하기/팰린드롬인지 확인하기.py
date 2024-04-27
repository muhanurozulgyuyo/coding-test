#10988 팰린드롬인지 확인하기

S = input()

S_rev = S[::-1]

if S == S_rev:
    print(1)
else:
    print(0)