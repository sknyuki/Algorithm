import sys
import itertools
input = sys.stdin.readline
N = int(input())
numlist = list(i for i in range(10))


for i in itertools.permutations(numlist, 7):
    h, e, l, o, w, r, d = i[0], i[1], i[2], i[3], i[4], i[5], i[6]
    if (h*10000+e*1000+l*100+l*10+o)+(w*10000+o*1000+r*100+l*10+d) == N and h != 0 and w != 0:
        print(' ', h*10000+e*1000+l*100+l*10+o)
        print('+', w*10000+o*1000+r*100+l*10+d)
        print('-------')
        print(f" {N:6}")
        exit()
print("No Answer")

