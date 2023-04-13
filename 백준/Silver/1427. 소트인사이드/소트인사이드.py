import sys
input = sys.stdin.readline
x = sorted(list(input()), reverse = True)
print(''.join(x))