import sys
input = sys.stdin.readline

AlphabetNumber = {'ABC': 1, 'DEF': 2, 'GHI': 3,
                  'JKL': 4, 'MNO': 5, 'PQRS': 6, 'TUV': 7, 'WXYZ': 8}
Sentence = input().strip()
result = 0


for i in Sentence:
    for y in AlphabetNumber:
        if i in y:
            result += AlphabetNumber[y]+2

print(result)
