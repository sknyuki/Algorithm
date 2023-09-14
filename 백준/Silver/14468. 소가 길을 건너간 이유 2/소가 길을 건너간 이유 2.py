import sys
input= sys.stdin.readline().strip()
result = 0 
for start in range(52): # 시작지점부터
    for end in range(start+1,52): # 그뒤 까지
        if input[start] == input[end]: # 알파벳이 같으면
            cows = input[start:end+1] # 그 사이에 있는 소 리스트
            for i in cows:
                if cows.count(i) == 1: # 만일, 소가 1번이라면 경로 상에서 만나게 되므로
                    result += 1 # 추가
            break # 같은 알파벳은 뒤에 추가로 나오지 않음
print(result // 2) # 겹치는수 셀 때 2배로 셋으니 //2 ex) -> (A,B)(B,A)