import sys
from itertools import combinations
input = sys.stdin.readline


def check(tmp_pass):
    v_count, c_count = 0, 0
    for i in tmp_pass:
        if i in vowels:#모음이면
            v_count += 1
        else:#모음이 아니면
            c_count += 1
    return v_count, c_count


L, C = map(int, input().split())
A = sorted(list(input().rstrip().split()))
tmp_list = list(combinations(A, L))#오름차순으로 리스트 콤비네이션
vowels = ['a', 'e', 'i', 'o', 'u']#모음인지 확인용


for tmp_pass in tmp_list:
    v_count, c_count = check(tmp_pass)
    if v_count >= 1 and c_count >= 2:#모음1개이상 and 자음2개 이상이면
        print(*tmp_pass, sep="")

