import sys
input=sys.stdin.readline

N=int(input())


#한 둘레마다 6의 배수만큼 수량이 증가 
#한둘레식 넓어질때 마다 N+1

a=1
n=1 

while a<N:
    a+=6*n
    n+=1
   
print(n)