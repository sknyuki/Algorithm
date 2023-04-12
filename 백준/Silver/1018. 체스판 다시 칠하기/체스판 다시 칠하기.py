import sys
input = sys.stdin.readline

N, M = map(int, input().split())
listC = [input().strip() for _ in range(N)]

# 체스판의 크기를 8*8로 잘라야한다
# 자른 형태로 이동을하게 됨
count = []

for i in range(N-7):
    for j in range(M-7):
        xdraw = 0  # W부터 시작이 되었을때
        ydraw = 0  # B부터 시작이 되었을떄

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if listC[a][b] != "W":
                        xdraw += 1
                    else:
                        ydraw += 1
                else:
                    if listC[a][b] != "B":
                        xdraw += 1
                    else:
                        ydraw += 1
        count.append(min(xdraw, ydraw))

print(min(count))
