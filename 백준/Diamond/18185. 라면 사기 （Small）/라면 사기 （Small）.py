import sys
input = sys.stdin.readline

n = int(input())
listA = list(map(int, input().split()))+[0, 0]

pay7 = 0
pay5 = 0
pay3 = 0
i = 0

while sum(listA) != 0:
    #print(i, listA, pay7, pay5, pay3)
    if listA[i+1] > listA[i+2] > 0 and listA[i] > 0:
        min5 = min(listA[i], listA[i+1]-listA[i+2])
        pay5 += min5
        listA[i] -= min5
        listA[i+1] -= min5
    if listA[i] > 0 and listA[i+1] > 0 and listA[i+2] > 0:
        min7 = min(listA[i:i+3])
        pay7 += min7
        listA[i] -= min7
        listA[i+1] -= min7
        listA[i+2] -= min7
    if listA[i] > 0 and listA[i+1] > 0:
        min5 = min(listA[i:i+2])
        pay5 += min5
        listA[i] -= min5
        listA[i+1] -= min5
    if listA[i] > 0:
        pay3 += listA[i]
        listA[i] = 0
    i += 1


test = pay7*7+pay5*5+pay3*3

print(test)
