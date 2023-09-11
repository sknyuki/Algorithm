def count_kills(count, time):
    A = list(map(int, input().split()))
    A.sort()
    resist_before = A[0]
    resist = 1

    for i in range(1, count):
        if A[i]-resist_before >= time:
            resist += 1
            resist_before = A[i]

    return resist


n, m = map(int, input().split())

E = count_kills(n, 100)
O = count_kills(m, 360)
print(E, O)
