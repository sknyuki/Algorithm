import sys
input = sys.stdin.readline

answer = [0] * 1001
triangleNum = []
for i in range(1, 45):
    triangleNum.append(i * (i + 1) // 2)

for a in triangleNum:
    for b in triangleNum:
        for c in triangleNum:
            if a + b + c <= 1000:
                answer[a + b + c] = 1

# print(answer)

T = int(input())
K = []
for _ in range(T):
    K.append(int(input()))

for target in K:
    print(answer[target])