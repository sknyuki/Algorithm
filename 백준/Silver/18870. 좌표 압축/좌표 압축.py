import sys
input = sys.stdin.readline
N = int(input())
listA = list(map(int, input().split()))
sortA = sorted(set(listA))

my_dict = {}
cnt = 0
for i in sortA:
    my_dict[i] = cnt
    cnt += 1

for i in listA:
    print(my_dict[i], end=" ")
