import sys
input = sys.stdin.readline

N, M = map(int, input().split())
change = reversed(list(int(input()) for _ in range(N)))

cnt = 0
for i in change:
    if M >= i:
        if M == 1:
            cnt+=1
            break
        else:
            temp, C = divmod(M, i)
            cnt += temp
            M = C



print(cnt)
