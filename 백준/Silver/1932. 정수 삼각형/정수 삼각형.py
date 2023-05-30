import sys
input=sys.stdin.readline

# TA[0]~[N]까지 더해가며 최댓값을 도출 
# 대각선의 방향으로만 내려올 수 있음 
# 원활하게 풀기위해 역순으로 삼각형의 아래에서부터 올라가며 접근 N->1
# i행의 0에 올수있는 최댓값-> TA[i][0]=max(TA[i+1][0],TA[i+1][1])+TA[i][0]
# 위 작업을 TA의 N-1번행부터 0번행의 모든 엘리멘트에 적용
N=int(input())
TA=[list(map(int,input().split())) for _ in range(N)]


for i in range(N-2,-1,-1):
    for j in range(len(TA[i])):
        TA[i][j]=max(TA[i+1][j],TA[i+1][j+1])+TA[i][j]

print(TA[0][0])
