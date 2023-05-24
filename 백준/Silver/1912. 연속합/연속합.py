import sys
input = sys.stdin.readline


N = int(input())
listA = list(map(int, input().split()))

for i in range(1,N): #[i]와 [i]+[i-1]을 비교하며 큰 값으로 [i]자리에 초기화
    listA[i]=max(listA[i],sum(listA[i-1:i+1]))
        
print(max(listA))
