import sys
input=sys.stdin.readline

A,B=map(int,input().split())

def solution(n, q):
    tmp="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rev_base = ''

    while n > 0:
        n, mod = divmod(n,q)
        rev_base += tmp[mod]

    return rev_base[::-1] 
    

print(solution(A, B))