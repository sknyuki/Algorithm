import sys
input = sys.stdin.readline

listA = list((int(input()) for i in range(5)))
listA.sort()

print(sum(listA)//5, listA[2])
