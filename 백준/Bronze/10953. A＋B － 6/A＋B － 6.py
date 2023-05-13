import sys
input = sys.stdin.readline
N = int(input())
answer = []
for i in range(N):
    answer.append(sum(map(int, input().split(","))))
print(*answer, sep="\n")
