import sys
from collections import deque
input = sys.stdin.readline

L = int(input())
nums = list(map(int, input().split()))
target = int(input()) # == n

nums.append(0)
nums.sort()

A = 0
for i in range(len(nums)-1) :
    if nums[i] == target or nums[i+1] == target:
        A = 0
        break
    elif nums[i] < target and target < nums[i+1]:
        #구간의 총개수는 (가능한 시작점 수 * 가능한 끝점의 수) - (시작점과 끝점이 같은 경우)
        A = (target - nums[i]) * (nums[i+1] - target) - 1
        break

print(A)