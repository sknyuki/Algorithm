import sys
input = sys.stdin.readline


result = 0
strn = ""
summ = 0
pozack = True
N = int(input())

while pozack:
    result += 1
    strn = str(result)
    listA = []
    for i in strn:
        listA.append(int(i))
    summ = sum(listA)+result
   # print(f"listA:{listA}, result:{result},summ:{summ}")
    if summ == N:
        print(result)
        pozack = False
    elif result == N:
        print(0)
        pozack = False
