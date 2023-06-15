import sys
from collections import deque
input = sys.stdin.readline

# 처음 주사위의 모든 면0
# 바닥이 0이면 주사위 색을 복사
# 바닥이 0이 아니면 주사위에 색 복사후 바닥 0

# 다이스 굴러가는 패턴
def roll(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1:  # 오른쪽으로 굴러갈때
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif dir == 2:  # 왼쪽
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif dir == 3:  # 위
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    else:  # 아래
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e


# 보드 좌표 이동
def start_game():
    global y
    global x
    # 동,서,남,북 순서
    vector = [[0, 1], [0, -1], [-1, 0], [1, 0]]

    for o in order:
        vy, vx = y+vector[o-1][0], x+vector[o-1][1]

        if 0 <= vy < N and 0 <= vx < M:
            roll(o)  # 범위 안에 있을때만 굴리기
            if Map[vy][vx] == 0:  # 보드의 값이 0이면
                Map[vy][vx] = dice[5]  # dice의 뒷면이 보드로

            else:
                dice[5] = Map[vy][vx]  # dice에 보드 넘버를 칠하고
                Map[vy][vx] = 0  # 0으로 초기화

            print(dice[0])
            y, x = vy, vx  # 현재의 위치값을 이동한 방향으로


N, M, y, x, k = map(int, input().split())
Map = [list(map(int, input().split()))for _ in range(N)]
order = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0]  # 주사위

start_game()
