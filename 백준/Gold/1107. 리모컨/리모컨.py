import sys
input=sys.stdin.readline


def check_possible(channel, broken):
    for num in str(channel):
        if num in broken:#망가진 버튼중에 채널이 있으면
            return False
    return True

def main():
    N = int(input())  # 이동하려는 채널
    M = int(input())  # 고장난 버튼의 개수
    if M > 0:
        broken_buttons = set(input().split())  # 고장난 버튼 입력
    else:
        broken_buttons = set() #빈칸처리

    answer = abs(N - 100)  # 초기값은 +나 - 버튼으로만 이동하는 경우
    for channel in range(1000001):#백만개의 채널중에
        if check_possible(channel, broken_buttons):
            # 현재 채널에서 n까지 +나 - 버튼으로 이동하는 횟수
            press = len(str(channel)) + abs(channel - N)
            answer = min(answer, press)

    print(answer)


main()