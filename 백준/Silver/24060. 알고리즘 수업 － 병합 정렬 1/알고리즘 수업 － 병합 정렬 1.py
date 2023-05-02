import sys
input = sys.stdin.readline


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = (len(arr)+1) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            answer.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            answer.append(high_arr[h])
            h += 1

    for i in range(l, len(low_arr)):
        answer.append(low_arr[i])
        merged_arr.append(low_arr[i])

    for j in range(h, len(high_arr)):
        answer.append(high_arr[j])
        merged_arr.append(high_arr[j])

    return merged_arr


answer = []
N, M = map(int, input().split())
listA = list(map(int, input().split()))


merge_sort(listA)


if len(answer) >= M:
    print(answer[M-1])
else:
    print(-1)