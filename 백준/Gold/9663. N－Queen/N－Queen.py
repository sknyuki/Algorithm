import sys
input= sys.stdin.readline
#######탐색 1행(n)부터 N행까지 내려가는 것으로 진행#######
#1.queen을 놓을 수 없는 조건 
# 1)같은 행&열에 퀸이 중복으로 올 수 없음
# 2)대각선상에 퀸이 중복으로 올 수 없음
#2.위 조건에 해당되는 visited처리가 필요
#3.v1(열 list길이 N),v2(우측상승 대각선 길이 2N-1),v3(우측하강 대각선 길이 2N-1)
#4.위 조건에 만족하면 True로 바꾼 후 dfs()실행 v1,v2,v3=0으로 초기화
#5.if n==N: cnt+=1 후 return으로 열성노드를 걷어냄 이후 위 3번 작업 실행 

#V1,V2,V3의 조건
# 1)V1 -> if v1[i]==0       같은 열 중복검사
# 2)v2 -> if v2[i+n]==0     i+n 값이 동일 우측 상승 대각선상에선 전부 동일 
# 3)v3 -> if v3[i-n]==0     i-n 값이 동일 우측 하강 대각선상에선 전부 동일

def dfs(n):
    global cnt
    if n==N:
        cnt+=1
        return
    for i in range(N): #가로 행의 길이만큼 세로 열탐색 진행
        if v1[i]==v2[i+n]==v3[i-n]==False:
            v1[i]=v2[i+n]=v3[i-n]=True
            dfs(n+1)#다음 행 탐색
            v1[i]=v2[i+n]=v3[i-n]=False




N=int(input())
cnt=0
v1=[False]*N
v2=[False]*(2*N-1)
v3=[False]*(2*N-1)

dfs(0)
print(cnt)