import sys
from collections import deque
input = sys.stdin.readline

x,y,p1,p2 = map(int,input().split())
cnt = 0
while 1:
	if p1 == p2:
		break
	if cnt > 1000:
		p1 = -1
		break
	if p1 > p2:
		p2 += y

	elif p1 < p2:
		p1 += x
	cnt += 1

print(p1)