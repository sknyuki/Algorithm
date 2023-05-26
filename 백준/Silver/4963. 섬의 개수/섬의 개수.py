import sys
from collections import deque
input = sys.stdin.readline


def bfs(y, x):
    # 방향 벡터
    vector = [[0, 1], [1, 0], [-1, 0], [0, -1],
              [1, 1], [-1, -1], [-1, 1], [1, -1]]
    que = deque()
    que.append([y, x])
    while que:
        # bfs탐색
        y, x = que.popleft()
        for vy, vx in vector:
            my, mx = vy+y, vx+x
            if 0 <= my < B and 0 <= mx < A and board[my][mx] == 1:
                board[my][mx] = 0
                que.append([my, mx])


while True:
    A, B = map(int, input().split())
    cnt = 0
    if A == B == 0:
        break
    else:
        board = [list(map(int, input().split())) for _ in range(B)]
        for i in range(B):
            for j in range(A):
                if board[i][j] == 1:
                    bfs(i, j)
                    cnt += 1
        print(cnt)
