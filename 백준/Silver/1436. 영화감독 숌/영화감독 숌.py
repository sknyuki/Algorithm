import sys
input = sys.stdin.readline

N = int(input())

number = 666
A = 1
if N == 1:
    print(666)
else:
    while A != N:
        number += 1
        if '666' in str(number):
            A += 1
    print(number)
