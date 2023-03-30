import sys
input = sys.stdin.readline

S = str(input().strip())
alphabet = 'abcdefghijklmnopqrstuvwxyz'


for i in range(len(alphabet)):
    print(S.find(alphabet[i]), end=" ")
