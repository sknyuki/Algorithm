import sys
input = sys.stdin.readline

N = int(input())
listA = sorted(list(int(input())for _ in range(N)))


for i in listA:
    print(i)
