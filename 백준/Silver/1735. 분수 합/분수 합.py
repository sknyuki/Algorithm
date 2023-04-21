import sys
input = sys.stdin.readline


def GCD(x, y):
    if y == 0:
        return x
    else:
        return GCD(y, x % y)


A, B = map(int, input().split())
C, D = map(int, input().split())


E = A*D+B*C
F = B*D
temp = GCD(F, E)
print(E//temp,
      F//temp)
