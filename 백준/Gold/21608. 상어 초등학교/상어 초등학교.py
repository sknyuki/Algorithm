import sys
from collections import deque
input = sys.stdin.readline

# 자리배치
# 1.vector 범위 내에  student[1:] 이후의 번호가 가장 많은 칸
# 2.vector 내부에 비어 있는 칸이 가장 많은 칸
# 3.2번도 만족하는 경우 lamda x(1),x(0)


def locate(like_list):
    locate = []
    for y in range(N):
        for x in range(N):
            if board[y][x] == 0:
                cnt = 0  # 빈칸 수
                likes = 0  # 좋아하는 학생 수
                #  자리가 있을때
                for vy, vx in vector:
                    my, mx = vy+y, vx+x
                    if 0 <= my < N and 0 <= mx < N:
                        if board[my][mx] == 0:  # 빈자리일때
                            cnt += 1
                        if board[my][mx] in like_list:  # 좋아하는 학생이 있을때
                            likes += 1
                locate.append([y, x, cnt, likes])
    # 빈칸,좋아하는 사람 순으로 정렬,열,행 순으로 정렬
    locate.sort(key=lambda x: (-x[3], -x[2], x[0], x[1]))
    return locate[0]  # 젤 앞 에꺼 반환


def point():
    answer = 0
    for y in range(N):
        for x in range(N):
            temp = 0
            for vy, vx in vector:
                my, mx = vy+y, vx+x
                if 0 <= my < N and 0 <= mx < N:
                    if board[my][mx] in student_list[board[y][x]]:  # 좋아하는 학생 리스트에 있으면
                        temp += 1
            if temp>0:
                temp = 10**(temp-1)  # 하나의 학생의 값
                answer += temp  # 전체 값에 반영
    return answer


N = int(input())
vector = [[0, 1], [1, 0], [-1, 0], [0, -1]]
board = [[0]*N for _ in range(N)]
list_locate = []  # 반환 값
student_list = {}  # 전체 학생 리스트

# 자리 배치
for _ in range(N**2):
    student = list(map(int, input().split()))
    number, like_list = student[0], student[1:]
    student_list[number] = like_list
    list_locate = locate(like_list)
    board[list_locate[0]][list_locate[1]] = number


# print(*board, sep="\n")
# print("=============")
# print(*student_list,sep="\n")
# print("=======================")

# 점수 출력
print(point())
