import sys
input = sys.stdin.readline

while True:
    A = int(input())
    listA = []
    if A == -1:
        break
    else:
        for i in range(1, A):
            if A % i == 0:
                listA.append(i)
        if sum(listA) == A:
            print(A, '=', end=' ')
            print(*listA, sep=' + ')

        else:
            print(f"{A} is NOT perfect.")
