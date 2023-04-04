import sys
input=sys.stdin.readline

N=int(input())

start=0
i=0
line=0
top=0
bottom=0
end=0
while N>end:
    start+=i
    i=1+i
    line+=1
    end=start+i
#    print(f"i:{i}, start:{start}, end:{end}, line:{line}")
    
count=end-N

if line%2==0:
    top=line-count
    bottom=count+1
else:
    top=count+1
    bottom=line-count

        
    
print(f"{top}/{bottom}")


