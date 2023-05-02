import sys
input = sys.stdin.readline

while True:
    try:
        N = int(input())
        if 0 <= N <= 12:
            line = "-"
            for i in range(N):
                line = line+" "*len(line)+line
            print(line)
        else:
            break
    except:
        break
