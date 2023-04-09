import sys
input = sys.stdin.readline

N = int(input())
X = []
Y = []
for i in range(N):
    A, B = map(int, input().split())
    X.append(A)
    Y.append(B)

print((max(X)-min(X))*(max(Y)-min(Y)))
