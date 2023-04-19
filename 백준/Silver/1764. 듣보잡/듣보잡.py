import sys
input = sys.stdin.readline
N, M = map(int, input().split())

my_dict = {}
result = []
for i in range(M+N):
    A = input().strip()
    if A not in my_dict.keys():
        my_dict[A] = 0
    else:
        result.append(A)

result.sort()
print(len(result))
for i in result:
    print(i)

