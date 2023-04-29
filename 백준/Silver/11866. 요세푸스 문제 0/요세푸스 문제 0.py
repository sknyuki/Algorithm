import sys
from collections import deque
input = sys.stdin.readline


A, B = map(int, input().split())
Cqueue = deque(i for i in range(1, A+1))
answer = []
for _ in range(A):
    Cqueue.rotate(1-B)
    answer.append(Cqueue.popleft())

print("<", end="")
print(*answer, sep=", ", end="")
print(">")
