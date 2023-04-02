import sys
input=sys.stdin.readline

listA=[]
Count=1
for i in range(10):
    listA.append((int(input()))%42)

listA.sort()
for i in range(9):
    if listA[i]!=listA[i+1]:
        Count+=1


print(Count)