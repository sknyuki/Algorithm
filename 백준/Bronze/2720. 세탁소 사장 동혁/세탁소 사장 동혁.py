import sys
input=sys.stdin.readline

N=int(input())
ChangeInput=[25,10,5,1]

#거스럼돈 중 액수가 큰 잔돈부터 나누었을때 
# if 잔돈/Quarter>0:
# n,y =divmod(잔돈(y),Quarter부터...) 
#n>0 and y>0 일때 y의 값이 0이 될때 까지 나누기 반복
for i in range(N):
    C=int(input())
    ChangeOut=[]
    x=0
    while C>0:
        if C/ChangeInput[x]>0:
            A,B=divmod(C,ChangeInput[x])
            ChangeOut.append(A)
            x+=1
            C=B
        else:
            x+=1
    while len(ChangeOut)!=4:
        ChangeOut.append(0)
        
    print(*ChangeOut)