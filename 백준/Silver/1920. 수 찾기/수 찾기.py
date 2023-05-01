import sys
input = sys.stdin.readline


def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return 1
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return 0


N = int(input())
data = list(map(int, input().split()))
M = int(input())
target_list = list(map(int, input().split()))
data.sort()
for i in target_list:
    print(binary_search(i, data))
