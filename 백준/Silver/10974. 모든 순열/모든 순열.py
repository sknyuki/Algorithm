import sys
input = sys.stdin.readline

N = int(input())
s = []


def dfs():
    if len(s) == N:
        print(' '.join(map(str, s)))
        return
    for i in range(1, N+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()


dfs()
