import sys
input = sys.stdin.readline
S = input().strip()
# 5+4+3+2+1
# S[0:1],S[1:2],S[2:3],S[3:4],S[4:5]
# S[0:2],S[1:3],S[2:4],S[3:5]
# S[0:3],S[1:4],S[2:5]
# S[0:4],S[1:5]
# S[0:5]
myset = set()

cnt = 1
for i in range(len(S)+1):
    for j in range(cnt, len(S)+1):
        myset.add(S[i: j])

    cnt += 1

print(len(myset))
