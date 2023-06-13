import sys
from collections import deque
input = sys.stdin.readline


# 이동 함수
# bfs로 초기 위치가 0이면 1로 바꾸고 cnt+=1 방향 설정및 이동 함수로 이동

# 방향 설정용 함수
# 디렉션:0,1,2,3
# 디렉션들 별로 vector 설정
# if 4개-> 0이면 진입 진입후 return y,x
# 다 돌아도 0이 없고 뒤가 1(벽)이 아니면 진입 d별로 후방
#  1이면 그대로 전체 종료


# 방향으로의 무빙
def move(y, x, vector, cnt):
    for vy, vx, d in vector:
        my, mx, d = y+vy, x+vx, d
        if 0 <= my < Y and 0 <= mx < X:
            if board[my][mx] == 0:  # 청소 할 곳이 나오면
                return my, mx, d  # 꺾은 방향으로의 이동과 이동후 바라볼 방향 return

    # 청소할 곳이 없으면
    # my,mx는 후면으로 d는 앞을 바라본채로
    my, mx, d = vector[1][0]+y, vector[1][1]+x, vector[3][2]
    if board[my][mx] == 3:  # 뒤로 진입이 되면(청소된 구역)
        return my, mx, d  # 뒤로 진입과 바라볼 방향 return
    elif board[my][mx] == 1:  # 뒤가 벽이면
        print(cnt)  # cnt print 후 종료
        exit(0)


def bfs(sy, sx, d):
    # vector 꺾을 방향과 꺾은 후 바라볼 방향
    vector0 = [[0, -1, 3], [1, 0, 2], [0, 1, 1], [-1, 0, 0]]
    vector1 = [[-1, 0, 0], [0, -1, 3], [1, 0, 2], [0, 1, 1]]
    vector2 = [[0, 1, 1], [-1, 0, 0], [0, -1, 3], [1, 0, 2]]
    vector3 = [[1, 0, 2], [0, 1, 1], [-1, 0, 0], [0, -1, 3]]

    global cnt
    que = deque()
    que.append([sy, sx])
    while que:
        y, x = que.popleft()
        if board[y][x] == 0:  # 청소를해야하면
            board[y][x] = 3  # 청소후 cnt+1
            cnt += 1
        if d == 0:  # 바라보는 방향에 따라 vecter 차별화
            y, x, d = move(y, x, vector0, cnt)
            que.append([y, x])
            continue
        if d == 1:
            y, x, d = move(y, x, vector1, cnt)
            que.append([y, x])
            continue
        if d == 2:
            y, x, d = move(y, x, vector2, cnt)
            que.append([y, x])
            continue
        if d == 3:
            y, x, d = move(y, x, vector3, cnt)
            que.append([y, x])
            continue


Y, X = map(int, input().split())
Sy, Sx, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(Y)]
cnt = 0

bfs(Sy, Sx, D)