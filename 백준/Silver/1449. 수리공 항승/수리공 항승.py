import sys
input = sys.stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

start = A[0]-0.5
end = start + L
cnt = 1
for i in range(N):
    if start >= A[i] or end <= A[i]:
        cnt += 1
        start = A[i]-0.5
        end = start + L

print(cnt)
