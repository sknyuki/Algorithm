import sys
input = sys.stdin.readline

N = int(input())
list = []

for i in range(0, (N//3)+1):
    for j in range(0, (N//5)+1):
        if 5*j+3*i == N:
            list.append(j+i)

if len(list) > 0:
    print(min(list))
else:
    print(-1)

