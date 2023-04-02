import sys
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
dy = [1,0,-1,0]
dx = [0,1,0,-1]
snail = [[0]*N for _ in range(N)]
anser=[]
D = 0
y,x = 0,0
for i in range(N*N,0,-1):
    snail[y][x] = i
    if i==K:
           anser=[(y+1),(x+1)]  
    ny, nx = y +dy[D], x + dx[D]
  
    if  0<=ny<N and 0<=nx<N and snail[ny][nx]==0:
        y, x = ny, nx
      
    else:
        D = (D+1) % 4
        y, x = y + dy[D], x + dx[D]
      

for m in snail:
    print(*m)
    
print(*anser)
