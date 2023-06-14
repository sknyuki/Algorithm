import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
city = list(list(map(int, input().split())) for _ in range(N))
result = 999999
house = []      # 집의 좌표
chick = []      # 치킨집의 좌표

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chick.append([i, j])

# 백트레킹 없이 combination으로 구현 치킨집 M개까지 감소
#print(list(combinations(chick, M)))
for c in list(combinations(chick, M)):  # m개의 치킨집 좌표
    temp = 0            # 도시의 치킨 거리
    for h in house:
        chi_len = 999   # 각 집마다 치킨 거리
        for j in range(M):
            chi_len = min(chi_len, abs(h[0] - c[j][0]) + abs(h[1] - c[j][1]))
        temp += chi_len
    result = min(result, temp)

print(result)
