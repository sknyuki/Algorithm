import sys
input = sys.stdin.readline


def solution(N):
    pn = [True]*(N+1)
    pn[0] = pn[1] = False
    for i in range(2, int(N**0.5)+1):
        if pn[i]:
            for j in range(i*i, N+1, i):
                pn[j] = False
    primes = list(i for i in range(len(pn)) if pn[i])
    return primes


def find_pn(N, M):
    answer = 0
    cnt = 0
    temp = 0
    while True:
        temp = primes_list[cnt]
        if N < temp <= M:
            answer += 1
        elif temp > M:
            break

        cnt += 1
    return answer


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
        print(find_pn(i, 2*i))
