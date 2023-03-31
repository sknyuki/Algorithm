import sys
input = sys.stdin.readline

Cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
# count로 Sentnce내부의 Cro의 값을 count후 number+1
# len(Sentence)-number

Sentence = input().strip()
number = 0

for i in Cro:
    number += Sentence.count(i)
#print(f"len(Sentence):{len(Sentence)},number:{number}")
print(len(Sentence)-number)
