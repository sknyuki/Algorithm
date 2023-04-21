import sys
input = sys.stdin.readline


def Greatest_common_divisor(x, y):
    if y == 0:
        return x
    else:
        return Greatest_common_divisor(y, x % y)


def Least_common_multiple(x, y):
    return (x*y)//Greatest_common_divisor(x, y)


A, B = map(int, input().split())
C, D = map(int, input().split())


F = Least_common_multiple(max(B, D), min(B, D))
E = A*(F//B)+C*(F//D)
temp = Greatest_common_divisor(max(F, E), min(F, E))
print(E//temp,
      F//temp)
