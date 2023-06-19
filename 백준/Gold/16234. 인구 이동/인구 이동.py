import sys
from collections import deque
input = sys.stdin.readline


def bfs(yy, xx):
    vector = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    que = deque()
    que.append([yy, xx])
    Union = [[yy, xx]]  # 연합
    visited[yy][xx] = 1
    while que:
        y, x = que.popleft()
        for vy, vx in vector:
            my, mx = vy+y, vx+x
            # 아직 방문을 안하였고
            if 0 <= my < N and 0 <= mx < N and not visited[my][mx]:
                if L <= abs(A[y][x]-A[my][mx]) <= R:  # 조건에 만족하면
                    visited[my][mx] = 1  # 방문처리후
                    Union.append([my, mx])  # Union 추가
                    que.append([my, mx])
    return Union


N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
answer = 0

while True:
    visited = [[0]*N for _ in range(N)]
    is_union = 0
    for y in range(N):
        for x in range(N):
            if visited[y][x] == 0:  # 방문을 하지 않은곳이 있다면
                Union = bfs(y, x)  # Union return
                if len(Union) > 1:  # 연합이 2개 이상이있다면
                    is_union = 1
                    population = sum(A[y][x] for y, x in Union) // len(Union)
                    for uy, ux in Union:  # 값을 평균 값으로 재배치
                        A[uy][ux] = population
    if is_union == 0:  # 연합이 없을때
        break
    answer += 1  # 하루가 지나면
print(answer)