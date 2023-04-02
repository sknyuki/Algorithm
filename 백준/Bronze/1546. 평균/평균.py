import sys
input=sys.stdin.readline


N=int(input())
Score=list(map(int,input().split()))
ModifyScore=[]
ModifyTotal=0
#성적들중 최댓값을 구한다 maxScore
#for 문을 사용하여 새로운 점수를 list에서 산출한다 (모든 점수를 점수/M*100)
#새롭게 산출된 리스트의 값들의 평균을 산출

MaxScore=max(Score)

for i in Score:
    ModifyScore.append((i/MaxScore)*100)
    

for i in ModifyScore:
    ModifyTotal+=i
    
print(ModifyTotal/N)