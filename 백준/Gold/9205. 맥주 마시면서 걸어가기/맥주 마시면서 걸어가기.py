from collections import deque


def bfs():
    q = deque()
    q.append((home_x, home_y))
    while q:
        x, y = q.popleft()
        if abs(x-festival_x) + abs(y-festival_y) <= 1000:
            print('happy')
            return
        for i in range(n):  # 편의점들 확인
            if not visited[i]:  # 편의점을 방문하지 않았다면
                new_x, new_y = graph[i]  # 편의점의 좌표를 새로 뽑고
                if abs(x-new_x) + abs(y-new_y) <= 1000:  # 다음거리까지 갈 수 있다면
                    visited[i] = 1  # 방문체크해주고
                    q.append((new_x, new_y))  # 큐에 담아준다
    print('sad')
    return


t = int(input())
for _ in range(t):
    n = int(input())
    home_x, home_y = map(int, input().split())
    graph = []
    for _ in range(n):
        x, y = map(int, input().split())
        graph.append((x, y))
    festival_x, festival_y = map(int, input().split())
    visited = [0 for _ in range(n+1)]
    bfs()
