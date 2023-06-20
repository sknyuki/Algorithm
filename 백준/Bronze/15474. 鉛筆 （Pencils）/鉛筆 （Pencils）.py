import sys
input=sys.stdin.readline

N,A,B,C,D=map(int,input().split())
cnt=0
result=0
answer1=0
answer2=0

while result<N:
    result=cnt*A
    cnt+=1
answer1=(cnt-1)*B

cnt=0
result=0
while result<N:
    result=cnt*C
    cnt+=1

answer2=(cnt-1)*D

print(min(answer1,answer2))