import sys
input = sys.stdin.readline

ChessA = (1, 1, 2, 2, 2, 8)
ChessB = list(map(int, input().split()))
Answer = [0]*len(ChessA)

for i in range(len(ChessA)):
    Answer[i] = ChessA[i]-ChessB[i]

print(*Answer)
