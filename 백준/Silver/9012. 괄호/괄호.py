import sys
input = sys.stdin.readline
N = int(input())

for _ in range(N):
    cnt = 0
    S = input().strip()
    if S[0] == ")" or S[-1] == "(":
        print("NO")
    else:
        for i in S:
            if i == "(":
                cnt += 1
            else:
                cnt -= 1
                if cnt < 0:
                    break
        if cnt == 0:
            print("YES")
        else:
            print("NO")
