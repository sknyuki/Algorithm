import sys
input=sys.stdin.readline
A,B=map(int,input().split())
if (A*100)>=B:
    print("Yes")
else:
    print("No")