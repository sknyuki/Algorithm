import sys
input = sys.stdin.readline
N = int(input())


for i in range(N):
    Sentence = (input().strip())
    for i in range(0, len(Sentence)-1):
        if Sentence[i] == Sentence[i+1]:
            pass
        elif Sentence[i] in Sentence[i+2:]:
            N -= 1
            break

print(N)
