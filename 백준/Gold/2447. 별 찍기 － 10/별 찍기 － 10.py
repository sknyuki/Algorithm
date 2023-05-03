import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

#위 중간 아래로 나눌것
#input 값을 3으로 나누어서 실행
# 1일경우 ['*']을 return->star
#listA생성
#하단코드를 실행
#위listA[0]:     for(Star(return값))문->i*3을 listA.append
#중간listA[1]:   for문->i+' '*len(star)+i 
#마지막listA[2]: 첫째줄listA[0]과 동일

def paint(N):
    temp=N//3
    if N==1:
        return '*'
    Star=paint(temp)
    global listA
    listA=[]

    for i in Star:
        listA.append(i*3)
    for i in Star:
        listA.append(i+' '*len(Star)+i)
    for i in Star:
        listA.append(i*3)
    return listA

N=int(input())
paint(N)
print(*listA ,sep='\n')
