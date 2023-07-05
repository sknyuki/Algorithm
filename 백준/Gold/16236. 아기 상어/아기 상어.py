import sys
from collections import deque
input = sys.stdin.readline

# 상어의 이동패턴
# 초기상태 크기 2
# 자신보다 작은것만 섭취가능 크기가 같으면 이동은 가능

# ->자신의 사이즈보다 작은 물고기가 없으면 end
# 자신의 사이즈 만큼 먹으면 크기+1
# 먹는 순서 ->가까운 순 ->칸수가 같으면 y,x의 값이 작은쪽 우선
# lamda로 처리


def bfs(y, x):
    global shark_age
    visited = [[0]*N for _ in range(N)]  # 방문 및 거리재기
    vector = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    catch_fish = []
    visited[y][x] = 1
    que = deque()
    que.append([y, x])
    while que:
        y, x = que.popleft()  # BFS로 접근
        for vy, vx in vector:
            my, mx = vy+y, vx+x
            if 0 <= my < N and 0 <= mx < N and not visited[my][mx]:
                if bowl[my][mx] <= shark_age:  # 상어보다가 이동이 가능하면
                    visited[my][mx] = visited[y][x]+1  # 이번 움직임의 방문처리
                    que.append([my, mx])  # 이동
                    if bowl[my][mx] and bowl[my][mx] < shark_age:  # 먹을 수 있으면
                        catch_fish.append(
                            [my, mx, visited[my][mx]-1])  # 일단 잡아놔

    # 가장 가까운 물고기순으로 반환
    catch_fish.sort(key=lambda x: (-x[2], -x[0], -x[1]))
    return catch_fish


N = int(input())
bowl = [list(map(int, input().split())) for _ in range(N)]
shark_age = 2  # 2살로 스타트
shark_tokken = 0
necessity_game = 0
result = 0
start_point_y, start_point_x = 0, 0

for y in range(N):
    for x in range(N):
        if 0 < bowl[y][x] < shark_age:  # 먹을게 있으면
            necessity_game = 1
        if bowl[y][x] == 9:
            start_point_y, start_point_x = y, x

if necessity_game:
    while True:
        catch_fish_sort = bfs(start_point_y, start_point_x)  # 잡은 물고기
        if not catch_fish_sort:  # 받은 내용물이 없으면(먹을 물고기가 없으면)
            print(result)
            break

        cy, cx, time = catch_fish_sort.pop()
        result += time  # 시간을 추가
        shark_tokken += 1  # 물고기를 먹고

        if shark_tokken == shark_age:  # 충분히 배불리 먹었으면
            shark_age += 1  # 나이를 먹고
            shark_tokken = 0  # 다시 배고파짐

        bowl[cy][cx], bowl[start_point_y][start_point_x] = 0, 0  # 먹은 처리
        start_point_y, start_point_x = cy, cx  # 상어의 자리를 이동

else:  # 처음부터 먹을 물고기가 없으면
    print(0)
