from collections import deque

vector = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def bfs(a, b):
    sheep = 0
    wolf = 0

    queue = deque()
    queue.append((a, b))

    if graph[a][b] == 'o':
        sheep += 1
    elif graph[a][b] == 'v':
        wolf += 1

    graph[a][b] = '#'

    while queue:
        x, y = queue.popleft()
        for vy, vx in vector:
            ny, nx = vy+y, vx+x
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != "#":
                if graph[nx][ny] == 'o':
                    sheep += 1
                elif graph[nx][ny] == 'v':
                    wolf += 1

                graph[nx][ny] = '#'
                queue.append((nx, ny))

    if wolf >= sheep:
        return 0, wolf
    elif sheep > wolf:
        return sheep, 0


r, c = map(int, input().split())
graph = []

ts = 0  
tw = 0  

for i in range(r):
    graph.append(list(input()))

for i in range(r):
    for j in range(c):
        if graph[i][j] in 'ov':
            tempSheep, tempWolf = bfs(i, j)
            ts += tempSheep
            tw += tempWolf

print(ts, tw)
