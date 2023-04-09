import sys
input = sys.stdin.readline

listA = []

for i in range(3):
    listA.append(int(input()))

listA.sort()

if listA.count(listA[0]) == len(listA):
    print("Equilateral")
elif sum(listA) == 180 and (listA[0] == listA[1] or listA[1] == listA[2]):
    print("Isosceles")
elif sum(listA) == 180 and (listA[0] != listA[1] and listA[1] != listA[2]):
    print("Scalene")
else:
    print("Error")
