import sys
input = sys.stdin.readline
k = int(input())

cnt = 0
choco1 = 0
ccnt = 0
while choco1 < k:
    cnt += 1
    choco1 = 2**cnt

choco = choco1
while True:
    if k >= choco:
        if k == choco:
            break
        k -= choco
        choco //= 2
        ccnt += 1

    else:
        choco //= 2
        ccnt += 1


print(choco1, ccnt)
