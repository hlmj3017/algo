def solution(participant, completion):
    # 이름을 개수로 저장하기 위한 딕셔너리 생성
    participant_dict = {}
    
    # 참가자 목록에서 이름을 카운트하여 딕셔너리에 저장
    for name in participant:
        if name in participant_dict:
            # 이미 딕셔너리에 존재하는 이름인 경우, 해당 이름의 개수를 1 증가시킴
            participant_dict[name] += 1
        else:
            # 딕셔너리에 존재하지 않는 이름인 경우, 딕셔너리에 추가하고 개수를 1로 초기화
            participant_dict[name] = 1
    
    # 완주자 목록에서 참가자를 빼기
    for name in completion:
        # 완주자의 이름을 딕셔너리에서 찾아 해당 이름의 개수를 1 감소시킴
        participant_dict[name] -= 1
    
    # 딕셔너리를 검사하여 값이 1인 이름이 완주하지 못한 선수
    for name, count in participant_dict.items():
        if count == 1:
            # 값이 1인 경우, 해당 선수는 완주하지 못한 선수임
            return name
        
print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))