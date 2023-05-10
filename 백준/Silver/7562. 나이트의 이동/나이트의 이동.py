import sys
from collections import deque
input = sys.stdin.readline


def bfs(y, x):
    if target == start:
        return 0
    vector = [[-2, 1], [-1, 2], [1, 2], [2, 1],
              [2, -1], [1, -2], [-1, -2], [-2, -1]]
    que = deque()
    que.append([y, x])
    while que:
        y, x = que.popleft()
        for vy, vx in vector:
            my, mx = y+vy, x+vx
            if 0 <= my <= I-1 and 0 <= mx <= I-1 and chess[my][mx] == 0:
                chess[my][mx] = chess[y][x]+1
                if chess[target[0]][target[1]] != 0:
                    return chess[my][mx]
                que.append([my, mx])


T = int(input())
for i in range(T):
    I = int(input())
    start = list(map(int, input().split()))
    target = list(map(int, input().split()))
    chess = [[0]*I for i in range(I)]
    print(bfs(start[0], start[1]))
