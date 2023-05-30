import sys
input=sys.stdin.readline

#1번은 2번과 달라야한다
#N과 N-1과 달라야한다
#(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
#-> 결국 인접한 집들간의 색은 달라야한다.

#RGB의 1번~N번 행까지 해당 행에 올 수 있는 최소값을 계속 갱신해 간다
# i행의0번 인덱스에 올 수 있는 최솟값 -> RGB[i][0]=min(RGB[i-1][1],RGB[i-1][2])+RGB[i][0]
# 위 작업을 3번 반복한다
N=int(input())
RGB=[list(map(int,input().split()))for _ in range(N)]

for i in range(1,N):
    RGB[i][0]=min(RGB[i-1][1],RGB[i-1][2])+RGB[i][0]
    RGB[i][1]=min(RGB[i-1][0],RGB[i-1][2])+RGB[i][1]
    RGB[i][2]=min(RGB[i-1][0],RGB[i-1][1])+RGB[i][2]

print(min(RGB[N-1]))