import sys
input = sys.stdin.readline

C = int(input())
for _ in range(C):
    List = list(map(int, input().split()))
    N = List[0]
    Score = List[1:]
    Aver = sum(Score)/N
    #print(f"총점수 {sum(Score)}")
    value = 0
    for i in Score:
        if i > Aver:
            value += 1
    # 비율 계산 특정값 / 전체값 * 100 = n%
    # print(f"aver:{Aver},value:{value}")
    print(f"{((value/N)*100):.3f}%")
