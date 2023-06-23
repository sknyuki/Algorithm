import sys
input=sys.stdin.readline

#n값을 입력 받음
# n+1을 2진수로 바꾼 후 맨 앞자리를 생략
# 0은 4로 1은 7로 치환

N=int(input())
num=format(N+1,'b')[1:]
print(num.replace('0','4').replace('1','7'))