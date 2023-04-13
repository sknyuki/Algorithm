import sys
input = sys.stdin.readline
S = input().strip()
K = ['K', 'O', 'R', 'E', 'A']
Y = ['Y', 'O', 'N', 'S', 'E', 'I']


for i in S:
    if i in K:
        K.remove(i)
        if len(K) == 0:
            print("KOREA")
            break
    if i in Y:
        Y.remove(i)
        if len(Y) == 0:
            print("YONSEI")
            break
