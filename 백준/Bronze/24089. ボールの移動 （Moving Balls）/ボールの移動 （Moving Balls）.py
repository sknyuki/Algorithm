import sys
input = sys.stdin.readline
A, B = map(int, input().split())
my_dict = {i+1: i+1 for i in range(A)}
move = [list(map(int, input().split())) for _ in range(B)]

for i in range(B):
    my_dict[move[i][0]] = move[i][1]

print(*my_dict.values(), sep="\n")
