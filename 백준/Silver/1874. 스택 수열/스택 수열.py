import sys
input = sys.stdin.readline
N = int(input())

result = []
temp = []

impossible = False
cnt=1
for _ in range(N):
    S = int(input())
    while cnt<=S:
            temp.append(cnt)
            result.append("+")
            cnt += 1
            
    if temp[-1]==S:
        temp.pop()
        result.append("-")
    else:  
        impossible=True
        break

if impossible:
    print("NO")
else:
    for i in result:
        print(i)
