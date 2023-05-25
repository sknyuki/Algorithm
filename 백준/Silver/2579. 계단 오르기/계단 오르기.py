import sys
input = sys.stdin.readline
# 연속합과 동일한 문제로 예상
# 조건상 연속되는 3번은 있을 수 없기에 연속되는 2번의 값과 한번을 도약한 값중 더 큰 값을 dp_list에 저장해 나감
#패턴
#arr    10  20  15 | 25  10  20
#cnt    1   2   3  | 4   5   6
#f(x)   10  30  35 | 50  65  65 f(cnt)=max(cnt-3)+arr(cnt-1)+arr(cnt) 
#h(x)   0   20  25 | 55  45  75 h(cnt)=max(cnt-2)+arr(cnt)
                

#dp의 3번째 값 까지는 하드코드로 넣어주고
#3번째 값부터 for문을 사용

N=int(input())
listA = list(int(input()) for _ in range(N))
dp=[0]*N
if N<3:
    print(sum(listA))
else:
    dp[0]=listA[0]
    dp[1]=listA[0]+listA[1]
    dp[2]=max(listA[0]+listA[2],listA[1]+listA[2]) #계단 max(1->3으로 온 경우, 2->3으로 온 경우)
    for i in range(3,N):
        dp[i]=max(dp[i-2]+listA[i],dp[i-3]+listA[i-1]+listA[i]) #패턴의 식 적용
    
    print(dp[-1])