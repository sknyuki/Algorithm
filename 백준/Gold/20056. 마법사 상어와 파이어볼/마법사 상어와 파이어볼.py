import sys
from collections import deque
input = sys.stdin.readline

# r, c, m, s, d
# r,c: 파이어볼의 위치
# m:질량
# d:방향
# s:속력

# 2개 이상의 파이어볼이 있는 경우
# 하나로 합쳐짐->4개로 분열
# m:sum(파이어볼.m)/5
# s:sum(파이어볼.s)/sum(len(파이어볼))
# d: if 전부 짝수 or 전부 홀수: 0,2,4,6
# else: 1,3,5,7
# if m==0: 소멸


def move(fireball):
    y, x, m, s, d = fireball[0]-1, fireball[1] - \
        1, fireball[2], fireball[3], fireball[4]

    # m:질량, s:속력, d:방향

    my, mx = (y+(vector[d][0]*s)) % N, (x +
                                        (vector[d][1]*s)) % N  # 처음과 끝이 연결되어있는 처리

    # board에 파이어볼 주입
    board[my][mx][0] += m  # 질량
    board[my][mx][1] += s  # 속력
    board[my][mx][2].append(d)  # 방향


N, M, K = map(int, input().split())
# N 판크기,M 볼갯수, K 이동명령횟수
# cnt,m,s,d 순
fireballs = [list(map(int, input().split())) for _ in range(M)]
even_odd = 0  # 방향 설정용
direction0246 = [0, 2, 4, 6]
direction1357 = [1, 3, 5, 7]
vector = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
result = 0

for _ in range(K):  # 移動回数
    board = [[[0, 0, []] for _ in range(N)] for _ in range(N)]
    for i in fireballs:
        move(i)  # board에 파이어볼들을 다 칠하면
    fireballs = []  # 파리어볼 초기화
    for y in range(N):
        for x in range(N):
            cnt = len(board[y][x][2])  # 파이어볼 갯수
            total_m = board[y][x][0]  # 총 질량
            total_s = board[y][x][1]  # 총 속력
            total_d = board[y][x][2]  # 총 방향
            if cnt > 1:  # 파이어볼이 여러개이면
                is_direction0246 = True
                fr, fc, fm, fs = y+1, x+1, total_m//5, total_s//cnt  # 좌표,질량,속력
                if fm != 0:  # 질량이 0이 아니면
                    for fd in range(cnt):
                        if fd == 0:
                            even_odd = total_d[fd] % 2
                        else:
                            if even_odd != total_d[fd] % 2:
                                is_direction0246 = False

                    # 방향값
                    if is_direction0246:  # 0246일때
                        for sep_d in direction0246:
                            fireballs.append([fr, fc, fm, fs, sep_d])
                    else:  # 1357일때
                        for sep_d in direction1357:
                            fireballs.append([fr, fc, fm, fs, sep_d])
                board[y][x] = [0, 0, []] #분열된 자리는 빈공간으로

    for y in range(N):#보드에 있는 모든 파이어볼을 다음루프에 투입
        for x in range(N):
            if board[y][x][0] != 0:
                fireballs.append([y+1, x+1, board[y][x][0], board[y]
                                 [x][1], board[y][x][2][0]])

for i in fireballs:#파이어볼의 모든 질량값을 더한 후 산출
    result += i[2]
print(result)
