import sys
N = int(sys.stdin.readline())
num = list(sys.stdin.readline().strip().split())
for i in range(N-1,-1,-1):
    for j in range(i):
        a, b = int(num[j] + num[j+1]), int(num[j+1] + num[j])
        if a < b:
            num[j], num[j+1] = num[j+1], num[j]
result = int("".join(num))
print(result)