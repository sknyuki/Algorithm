import sys
input=sys.stdin.readline

A,B,V=map(int,input().split())

Day=(V-B)/(A-B)

if Day==int(Day):
    print(int(Day))
else:
    print(int(Day)+1)