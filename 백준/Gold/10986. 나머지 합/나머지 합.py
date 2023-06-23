import sys
input=sys.stdin.readline

#누적합의 집합을 만들고
#카운팅(C)으로 M으로 나누었을때 같은 값을 가지는 집합을 만들어준다 
#인덱스의 값이 2이상일때
    #(M으로 나누었을때 같은 값을 가지는 값들이 2이상일때)
#C[i]C2(조합)+C[0](M으로 나누어 떨어질때)를 return

N,M=map(int,input().split())
A=list(map(int,input().split()))
S=[]
mysum=0
C=[0]*M #카운팅
answer=0
for i in A:#누적합을 구하고
    mysum+=i
    S.append(mysum)

for i in S: #나머지 집합을 만들고
    if i%M==0:
        answer+=1 #3으로 나누어 떨어질 때 +1
    C[i%M]+=1 #else가 아닌 if 다음에 넣어줘야함

for i in range(M):
    if C[i]>1:#2 이상이면 
        answer+=(C[i]*(C[i]-1))//2 #c[i]C2
print(answer)

