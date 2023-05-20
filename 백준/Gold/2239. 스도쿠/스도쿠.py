import sys
input = sys.stdin.readline


def row(x, a):
    for i in range(9):
        if a == board[i][x]:
            return False
    return True


def col(y, a):
    for i in range(9):
        if a == board[y][i]:
            return False
    return True


def rect(y, x, a):
    ny = y//3*3  # 0~2->0,3~5->3, 6~8->6 반환
    nx = x//3*3
    for i in range(3):
        for j in range(3):
            if a == board[ny+i][nx+j]:
                return False
    return True


def dfs(idx):
    if idx == len(point):
        for i in range(9):
            print(*board[i], sep="")
        exit(0)
    for i in range(1, 10):  # 빈칸에 들어갈 1부터 9까지의 숫자 탐색
        y = point[idx][0]  # 탐색할 y좌표
        x = point[idx][1]  # 탐색할 x좌표
        if row(x, i) and col(y, i) and rect(y, x, i):  # 모든 조건 만족하면
            board[y][x] = i  # 값을 보드에 반영
            dfs(idx+1)  # 다음 빈칸을 탐색
            board[y][x] = 0  # 초기화


board = [list(map(int, input().rstrip())) for _ in range(9)]

point = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            point.append([i, j])
dfs(0)
