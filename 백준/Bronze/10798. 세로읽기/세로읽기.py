import sys
input=sys.stdin.readline

listA=list(list((input().strip())) for _ in range(5))
Sentence=''

for i in range(15):
    for y in range(5):
        if i<len(listA[y]):
            Sentence+=listA[y][i]
print(Sentence)