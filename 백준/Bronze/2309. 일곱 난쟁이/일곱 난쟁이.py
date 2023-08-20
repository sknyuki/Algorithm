import sys

heights = []
for i in range(9):
    heights.append(int(sys.stdin.readline())) # 한줄에 여러 입력 값 

total = sum(heights)
one = 0
two = 0

for i in range(9):
    for j in range(i+1, 9):
        if total - (heights[i] + heights[j]) == 100:
            one, two = heights[i], heights[j]
            break

heights.remove(one)
heights.remove(two)
heights.sort() # 오름차순 정렬

# 출력
for i in heights:
    print(i)