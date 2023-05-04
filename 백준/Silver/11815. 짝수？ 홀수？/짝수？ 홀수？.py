import sys
input = sys.stdin.readline

# 어떠한 미지수 X의 약수 A,B 는 X/B=A 의 형태를 하고있음
# 따라서 X**0.5 까지만 로프를 돌면 모든 약수를 구할 수 있다.(제곱근이 A,B가 올수 있는 Max이기에)
# 하지만 이번과 같은 경우는 약수의 갯수가 홀짝 여부만 구하는것
# -> 제곱근이 정수인 경우는 자동으로 홀수


N = int(input())
listA = list(map(int, input().split()))

for i in listA:
    if i == int(i**0.5)**2:
        print(1, end=" ")
    else:
        print(0, end=" ")
