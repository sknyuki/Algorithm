import sys
input = sys.stdin.readline

N = input().strip()
set1 = [0]*10

for i in range(len(N)):
    num = int(N[i])
    if num == 6 or num == 9:
        if set1[6] <= set1[9]:
            set1[6] += 1
        else:
            set1[9] += 1
    else:
        set1[num] += 1

print(max(set1))
