import sys
input = sys.stdin.readline

x = []
y = []

for _ in range(3):
    A, B = map(int, input().split())
    x.append(A)
    y.append(B)


x.sort()
y.sort()
if x[0] == x[1]:
    x.append(x[2])
else:
    x.append(x[0])

if y[0] == y[1]:
    y.append(y[2])
else:
    y.append(y[0])

print(x[3], y[3])
