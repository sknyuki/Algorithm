import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
    A = input().strip()
    result = 0
    x = 0
    for j in range(len(A)):
        if A[j] == "O":
            result += A[x:j+1].count("O")
        else:
            result += 0
            x = j
        # print(result)
    print(result)
