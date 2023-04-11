import sys
input = sys.stdin.readline


def solution(x):
    listA = []
    for i in str(x):
        listA.append(int(i))
    return(x+(sum(listA)))


Set = list(i for i in range(1, 10001))

for i in range(1, 10001):
    if solution(i) in Set:
        Set.remove(solution(i))

for i in Set:
    print(i)
