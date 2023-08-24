import sys
input = sys.stdin.readline
T = int(input())

def gcd_for(a,b) :
    while b > 0 :
        tmp = a%b
        a = b
        b = tmp
    return a

def gcd_r(a,b) :
    if b == 0 :
        return a
    else :
        return gcd_r(b,a%b)

def lcm(a,b) :
    return a*b//gcd_r(a,b)

for _ in range(T) :
    a, b = map(int,input().split())
    print(lcm(a,b),gcd_r(a,b))