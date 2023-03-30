import sys
input = sys.stdin.readline


# 바구니 1~N번개

# M번 바구니 회전 (i회전j k)->(j k i)  (1   6   4)-> (6 7)
# 회전될 범위를 지정(begin~mid~end)
n, m = map(int, input().split())
box = [i+1 for i in range(n)]
for _ in range(m):
  i,j,k = map(int, input().split())
  box=box[:i-1]+box[k-1:j]+box[i-1:k-1]+box[j:]
for b in box:
  print(b, end=' ')