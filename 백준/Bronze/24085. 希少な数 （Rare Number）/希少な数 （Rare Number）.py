import sys
input = sys.stdin.readline

yacha={}
N=int(input())
S=list(map(int,input().split()))
S.sort()

for i in S:
    if i not in yacha.keys():
        yacha[i]=1
    else:
        yacha[i]+=1

print(min(yacha, key=yacha.get))
