import sys
input=sys.stdin.readline

listA=list([0]*9 for i in range(9))
MaxN=[]
MaxDict={}

for row in range(9):
    listA[row]=list(map(int,input().split()))

for i in range(9):
    MaxN.append(max(listA[i]))
    MaxDict[i]=listA[i].index(max(listA[i]))
    #print(f"{i}번째의 최대수값 위치:{listA[i].index(max(listA[i]))}")

MaxX=MaxN.index(max(MaxN))
MaxY=MaxDict[MaxX]
#print(MaxDict)
#print(MaxN)  
print(max(MaxN))
print(MaxX+1,MaxY+1)