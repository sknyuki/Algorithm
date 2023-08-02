import sys
input = sys.stdin.readline

N = int(input())
ANA = list(map(int, input().split()))
benefit, result = 0, 0	# 이익 최댓값, 결과값 0으로 초기화

for i in range(N-1, -1, -1) :	# 리스트를 뒤에서 진행
    benefit = max(benefit, ANA[i])	# 주가 최댓값 찾기
    result = max(result, benefit - ANA[i])	# 주가 최댓값 - i번째 주가

print(result)