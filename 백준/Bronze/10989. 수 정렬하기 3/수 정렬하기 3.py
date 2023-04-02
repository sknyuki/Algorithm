import sys
input = sys.stdin.readline

N = int(input())

result=[0]*10000
# for문을 돌면서 N값만큼 인자를 받아야함 (arr에 저장)
for _ in range(N):
    result[int(input())-1]+=1

    # 받은 인자중 가장 큰 값(max(arr)) 만큼 배열[0]배열(result)을 만들어줌
    # **만일 리소스 문제 걸리면 max값을 그냥 10000으로 잡고 for문


# for result의 갯수 i만큼
# 만일 값이 result[i]가 0인경우는 패스
#print(result)

for i in range(len(result)):
    if result[i] == 0:
        pass
    else:
        for _ in range(result[i]):
            print(i+1)
