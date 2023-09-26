# 최소한의 키누름 횟수 계산
# 문자열 target의 각 문자마다 keymap에서 가장 짧은 index를 찾아 sum 해주고
# 입력할 수 없는 문자열이 포함되어 있다면 반복문을 멈추고 sum=-1을 반환
def solution(keymap, targets):
    answer = []    # 결과를 저장할 리스트
    keydict = {}   # keymap을 기반으로 각 문자가 어떤 키에 할당되었는지 저장하는 딕셔너리
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            keys = keymap[i][j]
             # 문자가 keydict에 없으면 해당 문자를 키로 추가하고 현재 키 인덱스 + 1 값을 할당
            if keys not in keydict:
                keydict[keys] = j + 1
            # 이미 있는 문자인 경우  더 작은 키 누름 횟수로 업데이트
            else:
                keydict[keys] = min(keydict[keys], j+1)           
    # 각 문자열에 대해 최소한의 키 누름 횟수 계산
    for target in targets:
        sum=0
        for t in target:
            if t in keydict:
                sum += keydict[t]  # 문자가 keydict에 있으면 최소 누름 횟수를 더함
            else:
                sum = -1   # 문자가 keydict에 없으면 작성 불가능하므로 -1로 설정
                break      # 반복문 종료
        answer.append(sum) # 문자열을 작성하기 위한 누름 횟수를 결과 리스트에 추가

    return answer

print(solution(["ABACD", "BCEFD"],["ABCD","AABB"]))
print(solution(["AA"],["B"]))
print(solution(["AGZ", "BSSS"],["ASA","BGZ"]))