import sys
input=sys.stdin.readline


n, m = map(int,input().split())

A = list(map(int, input().split()))


start, end = 0, 1


count = 0

while start <= end and end <= n:

  
    total = sum(A[start:end])


    if total < m:

        end += 1


    elif total > m:

        start += 1


    else:

        count += 1

        end += 1

print(count)