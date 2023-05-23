import sys
input=sys.stdin.readline


S=list(input().strip().split("-")) # "-"를 구분자로 전부 찢어서 S에 받는다
sum_values=[]

for i in range(len(S)):
    if '+'in S[i]:  #   만일 내부에"+"가 있으면
        temp=list(S[i].split("+")) # "+"를 구분자로 나눈 후 temp에 담는다
        sum_value=0
        for j in range(len(temp)):
            sum_value+=int(temp[j])
        S[i]=sum_value # temp내부의 값을 다 더한 후 S집합의 해당 인덱스로 치환 
    else:
        S[i]=int(S[i]) #내부의 값들 전부 int타입으로 변환


result=S[0]
for i in range(1,len(S)):#첫번째 인덱스의 값부터 그 이후의 값들을 전부 빼줌
    result-=S[i]
print(result)
