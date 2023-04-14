import sys
input = sys.stdin.readline
N = int(input())


listS = list(input().strip() for _ in range(N))
my_set = list(set(listS))  # 중복 제거

my_set.sort(key=lambda X: (len(X), X))


for i in my_set:
    print(i)
