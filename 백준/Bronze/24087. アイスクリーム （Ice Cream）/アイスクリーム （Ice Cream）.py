import sys
input = sys.stdin.readline

S = int(input())
A = int(input())
B = int(input())

cnt = 1

while (S-A) > B*cnt:
    cnt += 1

if S <= A:
    print(250)
else:
    print(250+cnt*100)
