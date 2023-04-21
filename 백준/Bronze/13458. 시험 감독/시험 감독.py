import sys
input = sys.stdin.readline
N = int(input())
listA = list(map(int, input().split()))
A, B = map(int, input().split())

cnt = len(listA)
for i in listA:
    i -= A
    if i>0:
     if i % B == 0:
        cnt += i//B
     else:
        cnt += (i//B)+1
print(cnt)
