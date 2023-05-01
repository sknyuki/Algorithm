import sys
input = sys.stdin.readline
x = int(input())  
cnt = [0]*(x+1) 

for i in range(2, x+1):  # 2부터 x까지 반복
   # print("1뺴는 연산", i, cnt[i], cnt[i-1]+1)
    cnt[i] = cnt[i-1]+1  # 1을 빼는 연산 -> 1회 진행

    if i % 2 == 0:  # 2로 나누어 떨어질 때, 2로 나누는 연산
       # print("2 연산", i, cnt[i], cnt[i//2]+1)
        cnt[i] = min(cnt[i], cnt[i//2]+1)

    if i % 3 == 0:  # 3으로 나누어 떨어질 때, 3으로 나누는 연산
       # print("3 연산", i, cnt[i], cnt[i//3]+1)
        cnt[i] = min(cnt[i], cnt[i//3]+1)

print(cnt[x])
