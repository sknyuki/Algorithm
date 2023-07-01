import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))


print(sum(A[0:A.index(max(A))]))
print(sum(A[A.index(max(A))+1:]))
