import sys
from collections import deque
input= sys.stdin.readline


#graph는 끝과 처음이 이어져있음 -> my,mx의 이동 반경에 범위제한이 사라짐
#방향 벡터를 지시한 방향대로 설정  ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 
#물 복사 A[r][c] 기준 ↖, ↗, ↘, ↙ 방향에 있는 물바구니 수만큼 물이 증가
# 단 이때는 my,mx의 이동 반경에 제한을 줘야한다.
#저장된 물의 양이 2인 바구니는 구름이 생기며 물이-2 (구름이 있던 칸 제외)


def solution():
    #구름 이동 벡터(이동 제한없음)
    c_vector_y=[0,-1,-1,-1,0,1,1,1]
    c_vector_x=[-1,-1,0,1,1,1,0,-1]
    #물복사 벡터(이동 제한있음)
    w_increase_vector=[[-1,-1],[-1,1],[1,1],[1,-1]]

    #queue의 생성 및 구름시작 point 설정
    que=deque()
    que.extend([[N-1,0],[N-1,1],[N-2,0],[N-2,1]])

     #이동 방향 및 루프 생성
    for a,b in cm:
        visited=[[0]*N for _ in range(N)]
        cloud_disappear=[]
        #이동할 값 point(돌때마다 que값을 append 새로운 que점 입력)
        for y,x in que:
            my,mx=(c_vector_y[a-1]*b+y)%N,(c_vector_x[a-1]*b+x)%N #그래프는 연결되어있길래 나머지연산으로 이동반경 반영
            #이동후 물의 양 증가
            graph[my][mx]+=1
            cloud_disappear.append([my,mx])
            visited[my][mx]=1
  

        #이동 후 물 복사(비바라기 후 시작해야 하기에 for문 밖에 배치)
        for y,x in cloud_disappear:
            cnt=0
            for wy,wx in w_increase_vector:
                wcy,wcx=wy+y,wx+x
                #대각선 방향 물바구니에 물이있으면 count+=1
                if 0<=wcy<N and 0<=wcx<N and graph[wcy][wcx]!=0:
                        cnt+=1
            graph[y][x]+=cnt

        #구름 생성 for문 돌려서 -2  
        new_que=[] 
        for q in range(N):
             for w in range(N):  
                if not visited[q][w] and graph[q][w]>=2:
                  graph[q][w]-=2
                  new_que.append([q,w])
                  
        que=new_que #que 초기화
    
                
N,M=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(N)]
cm= [list(map(int,input().split()))for _ in range(M)]

solution()

result=0
for i in range(N):
    result+=sum(graph[i])
print(result)
