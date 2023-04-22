import sys
input = sys.stdin.readline


def solution(N):
    pn = [True]*(N+1)
    pn[0] = pn[1] = False
    for i in range(2, int(N**0.5)+1):
        if pn[i]:
            for j in range(i*i, N+1, i):
                pn[j] = False
    return pn


input_list = []
while True:
    N = int(input())
    if N == 0:
        break
    input_list.append(N)

primes_list = solution(max(input_list)*3)

for i in input_list:
    if i == 1:
        print(1)
    else:
        print(primes_list[i+1:2*i+1].count(True))
