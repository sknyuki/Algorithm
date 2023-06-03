import sys
input=sys.stdin.readline

#       A C A Y K P
#     0 0 0 0 0 0 0
#   C 0 0 1 1 1 1 1
#   A 0 1 1 2 2 2 2
#   P 0 1 1 2 2 2 3
#   C 0 1 2 2 2 2 3 
#   A 0 1 2 3 3 3 3
#   K 0 1 2 3 3 4 4

# solution
# 1)세로열(B)하나씩 가로행(A)탐색 
# 2)B[i]==A[j]이면 dp[i][j]=dp[i-1][j-1]+1
# 3)아닐 경우 max(dp[y][x-1],dp[y-1][x])를 반영


A=list(input().strip())
B=list(input().strip())
AN=len(A)+1
BN=len(B)+1

dp=[[0]*AN for _ in range(BN)] #2차 배열 생성

for y in range(1,BN):
    for x in range(1,AN):
        if A[x-1]==B[y-1]: #solution 과정 1
            dp[y][x]=dp[y-1][x-1]+1 #solution 과정 2
        else:
            dp[y][x]=max(dp[y][x-1],dp[y-1][x]) #solution 과정 3

#print(*dp,sep="\n")
print(dp[BN-1][AN-1])
