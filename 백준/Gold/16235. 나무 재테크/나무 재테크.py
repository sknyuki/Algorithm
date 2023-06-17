import sys
input = sys.stdin.readline

# 봄
# 자신의 나이 만큼 양분을 먹음(자신이 속 해 있는 칸안에 있는 양분만)
# age+1
# 나이가 어린애 순서로 양분 소모
# 적은애 우선 ->나이 많은애
#   자신의 나이 만큼 양분을 못 먹으면 사망

# 여름(양분)
# 운명을 달리 한 나무는 자신의 나이의 절반 만큼 양분으로 환원 된다.(소숫점 아래는 버린다)

# 가을(번식 기간)
# 나이가 5의 배수면 인접한 8개의  칸에 나이가 1인 나무가 생긴다.
# ((r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1))

# 겨울
# 땅에 양분을 추가 해준다.
# 양분의 양은 A[r][c]


def grow(food, tree):
    # 봄
    for i in range(N):
        for j in range(N):
            if tree[i][j]:
                grow_tree = []
                dead_tree = 0
                tree[i][j].sort()  # 나이순으로 정렬
                for t in tree[i][j]:
                    if t <= food[i][j]:  # 양분이 충분하면
                        food[i][j] -= t
                        t += 1
                        grow_tree.append(t)
                    else:
                        dead_tree += (t//2)  # 불충분하면
                tree[i][j] = grow_tree
                # 여름
                food[i][j] += dead_tree

    # 가을
    for y in range(N):
        for x in range(N):
            if len(tree[y][x]) == 0:  # 나무가 없으면 다음칸
                continue
            for t in tree[y][x]:
                if t % 5 == 0:  # 5의 배수이면
                    for vy, vx in vector:
                        my, mx = vy+y, vx+x
                        if 0 <= my < N and 0 <= mx < N:
                            tree[my][mx].append(1)  # 1살 묘목을 8방향에 추가

    # 겨울
    for y in range(N):
        for x in range(N):
            food[y][x] += feed[y][x]  # 양분을 추가해준다


N, M, K = map(int, input().split())
feed = [list(map(int, input().split()))for _ in range(N)]
tree_coordinate = [list(map(int, input().split())) for _ in range(M)]
food = [[5]*N for _ in range(N)]  # 양분
tree = [[[] for _ in range(N)] for _ in range(N)]
cnt = 0

for i in tree_coordinate:  # 초기 나무 위치
    tree[i[0]-1][i[1]-1].append(i[2])


vector = [[1, 1], [-1, -1], [1, 0], [0, 1], [-1, 0], [0, -1], [1, -1], [-1, 1]]

for _ in range(K):
    grow(food, tree)


for i in tree:
    for j in i:
        cnt += len(j)
print(cnt)
