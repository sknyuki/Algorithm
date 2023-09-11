def count_kills(n, m, d, s):
    s.sort()
    d.sort()
    E_before = d[0]
    O_before = s[0]
    E_kills = 1
    O_kills = 1

    for i in range(1, n):
        if d[i]-E_before >= 100:
            E_kills += 1
            E_before = d[i]
    for j in range(1, m):
        if s[j]-O_before >= 360:
            O_kills += 1
            O_before = s[j]

    return [E_kills, O_kills]


n, m = map(int, input().split())
d = list(map(int, input().split()))
s = list(map(int, input().split()))

result = count_kills(n, m, d, s)
print(*result)
