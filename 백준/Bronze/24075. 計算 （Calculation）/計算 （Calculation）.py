import sys
input = sys.stdin.readline

A,B=map(int,input().split())
print(max(A+B,A-B))
print(min(A+B,A-B))
