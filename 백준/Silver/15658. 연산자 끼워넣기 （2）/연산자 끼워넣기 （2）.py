import sys
input = sys.stdin.readline

#   retun조건?
#   파라미터?

#   함수의 파라미터
#   1)rerutn을 끝내줄 조건인 cnt(num의 선택을위한 idex척도)
#   2)dfs 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)의 사용 횟수를 알기위한 척도
#   3)현재의 계산값인 total값

#   매 계산마다 max와 min값을 최신화

#   각 연산들의 사용횟수가 op_list의 각 연산의 수치보다 작을시 연산 후 total값 최신화
#   재귀로 값을 다음 루프로 넘겨줌


def dfs(cnt, add, sub, mult, div, total):
    global result_max
    global result_min
    #   cnt가 num_list의 수치가 같아졌을때 return
    if cnt == N:
        #   max,min 최신화
        result_max = max(result_max, total)
        result_min = min(result_min, total)
        return
    #   다음 루프로 전송할 파라미터 계산
    if add < op_list[0]:
        dfs(cnt+1, add+1, sub, mult, div, total+num_list[cnt])
    if sub < op_list[1]:
        dfs(cnt+1, add, sub+1, mult, div, total-num_list[cnt])
    if mult < op_list[2]:
        dfs(cnt+1, add, sub, mult+1, div, total*num_list[cnt])
    if div < op_list[3]:
        dfs(cnt+1, add, sub, mult, div+1, int(total/num_list[cnt]))


N = int(input())
num_list = list(map(int, input().split()))
op_list = list(map(int, input().split()))

# 연산이 없을 경우에도 출력할 수치를 설정
result_max = -1000000000
result_min = 1000000000

dfs(1, 0, 0, 0, 0, num_list[0])

print(result_max)
print(result_min)

