import sys
input = sys.stdin.readline
listN = int(input())
output = list(map(int, input().split()))

cnt = 0
while sum(output) != 0:
    for i in range(len(output)):
        if output[i] % 2 == 1:
            output[i] -= 1
            cnt += 1
           # print(output)
    if sum(output) == 0:
        break
    for j in range(len(output)):
        output[j] //= 2
        # print("2나누기", output)
    cnt += 1
print(cnt)
