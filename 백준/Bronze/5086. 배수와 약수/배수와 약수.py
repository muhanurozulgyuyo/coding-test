import sys

a = 999
b = 999

while a != 0 and b != 0:
    a, b = map(int, sys.stdin.readline().split())
    if a > b:
        if a % b == 0:
            print('multiple')
        else:
            print('neither')
    elif a < b:
        if b % a == 0:
            print('factor')
        else:
            print('neither')