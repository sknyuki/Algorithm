import sys
from collections import deque
N, K= map(int, sys.stdin.readline().split())
queue = deque()
queue.append(N)
way = [0]*100001 
while queue:
    a =  queue.popleft()
    if a == K: 
        result = way[a]
        break
    
    for i in [a*2, a-1, a+1]:
        if 0 <= i < 100001 and way[i] == 0:
            if i == a*2 :
                way[i] = way[a]
                queue.append(i) 
            else : 
                way[i] = way[a] + 1
                queue.append(i)
print(result)