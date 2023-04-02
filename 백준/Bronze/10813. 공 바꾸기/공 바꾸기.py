import sys
input=sys.stdin.readline

N,M=map(int,input().split())

Basket=[]

for i in range(N):
    Basket.append(i+1)

for x in range(M):
    i,j=map(int,input().split())
    A=Basket[i-1]
    Basket[i-1]=Basket[j-1]
    Basket[j-1]=A
    
for i in Basket:
    print(i ,end=' ')