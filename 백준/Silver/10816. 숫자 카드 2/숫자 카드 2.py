import sys
input = sys.stdin.readline
A = int(input())
listA = list(map(int, input().split()))

B = int(input())
listB = list(map(int, input().split()))
my_dict = {i: 0 for i in listA}


for i in listA:
    my_dict[i] += 1


for j in listB:
    try:
        print(my_dict[j], end=" ")
    except:
        print(0, end=" ")
