import sys
input = sys.stdin.readline

Dict = {"A+": 4.5,
        "A0": 4.0,
        "B+": 3.5,
        "B0": 3.0,
        "C+": 2.5,
        "C0": 2.0,
        "D+": 1.5,
        "D0": 1.0,
        "F": 0.0}

A=''
B=''
C=''
Ns=0
Ss=0
for _ in range(20):
       A,B,C=map(str,input().strip().split())
       if C!='P':
        Ns+=float(B)*Dict[C]
        Ss+=float(B)
print(Ns/Ss)

